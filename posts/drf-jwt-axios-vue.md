---
date: "2018-04-21"
description: Getting DRF, JWT, Axios, and Vue to play nice
published: true
slug: drf-jwt-axios-vue
tags:
  - python
  - django
  - django-rest-framework
  - Vue.js
  - javascript
time_to_read: 3
title: Authenticating via JWT using Django, Axios, and Vue
---

![VueJS Logo](/images/vuelogo.png)

Getting Django Rest Framework, JWT, Axios, and Vue.js to play nice isn't easy. Here's my quick-and-dirty cheatsheet that I wrote while glueing the pieces together.

Note: My architecture doesn't use django-webpack-loader. Instead, I'm running Django and Vue.js as two separate projects. I do this because I **much prefer** generating new projects with `vue create` over configuring webpack.

## The Back-End

First, install some Django parts using the installer of your choice:

```bash
pip install Django
pip install djangorestframework
pip install django-cors-headers
pip install djangorestframework-jwt
```

Then, configure Django in `settings.py`:

```python
INSTALLED_APPS = (
    ...
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
)

MIDDLEWARE_CLASSES = (
  ...
  'corsheaders.middleware.CorsMiddleware',
)

CORS_ORIGIN_ALLOW_ALL = False
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_WHITELIST = (
    # TODO - set this properly for production
    'https://127.0.0.1:8080',
    'https://127.0.0.1:8000',
)

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        # By default we set everything to admin,
        #   then open endpoints on a case-by-case basis
        'rest_framework.permissions.IsAdminUser',
    ),
    'TEST_REQUEST_RENDERER_CLASSES': (
        'rest_framework.renderers.MultiPartRenderer',
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.TemplateHTMLRenderer'
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 20,
}

from datetime import timedelta

JWT_AUTH = {
    'JWT_ALLOW_REFRESH': True,
    'JWT_EXPIRATION_DELTA': timedelta(hours=1),
    'JWT_REFRESH_EXPIRATION_DELTA': timedelta(days=7),
}
```

Once that's done, it's time to do modify the `urls.py`:

```python
from django.conf.urls import include, url
...

urlpatterns = [
    ...
    # JWT auth
    url(r'^api/v1/auth/obtain_token/', obtain_jwt_token),
    url(r'^api/v1/auth/refresh_token/', refresh_jwt_token),
    # The rest of the endpoints
    url(r'^api/v1/', include('project.api', namespace='apiv1')),
    ...
]
```

Run the tests and fix them as they fail.

## The Front-End

First off, add this to your Vuex store:

```javascript
import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";

Vue.use(Vuex);

// Make Axios play nice with Django CSRF
axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFToken";

export default new Vuex.Store({
  state: {
    authUser: {},
    isAuthenticated: false,
    jwt: localStorage.getItem("token"),
    endpoints: {
      // TODO: Remove hardcoding of dev endpoints
      obtainJWT: "https://127.0.0.1:8000/api/v1/auth/obtain_token/",
      refreshJWT: "https://127.0.0.1:8000/api/v1/auth/refresh_token/",
      baseUrl: "https://127.0.0.1:8000/api/v1/",
    },
  },

  mutations: {
    setAuthUser(state, { authUser, isAuthenticated }) {
      Vue.set(state, "authUser", authUser);
      Vue.set(state, "isAuthenticated", isAuthenticated);
    },
    updateToken(state, newToken) {
      // TODO: For security purposes, take localStorage out of the project.
      localStorage.setItem("token", newToken);
      state.jwt = newToken;
    },
    removeToken(state) {
      // TODO: For security purposes, take localStorage out of the project.
      localStorage.removeItem("token");
      state.jwt = null;
    },
  },
});
```

Then, in a Vue component called something like `components/Login.vue`:

```html
<template lang="html">
  <form class="login form">
    <div class="field">
      <label for="id_username">Username</label>
      <input
        v-model="username"
        type="text"
        placeholder="Username"
        autofocus="autofocus"
        maxlength="150"
        id="id_username"
      />
    </div>
    <div class="field">
      <label for="id_password">Password</label>
      <input
        v-model="password"
        type="password"
        placeholder="Password"
        id="id_password"
      />
    </div>
    <button @click.prevent="authenticate" class="button primary" type="submit">
      Log In
    </button>
  </form>
</template>

<script>
  import axios from "axios";

  export default {
    data() {
      return {
        username: "",
        password: "",
      };
    },
    methods: {
      authenticate() {
        const payload = {
          username: this.username,
          password: this.password,
        };
        axios
          .post(this.$store.state.endpoints.obtainJWT, payload)
          .then((response) => {
            this.$store.commit("updateToken", response.data.token);
            // get and set auth user
            const base = {
              baseURL: this.$store.state.endpoints.baseUrl,
              headers: {
                // Set your Authorization to 'JWT', not Bearer!!!
                Authorization: `JWT ${this.$store.state.jwt}`,
                "Content-Type": "application/json",
              },
              xhrFields: {
                withCredentials: true,
              },
            };
            // Even though the authentication returned a user object that can be
            // decoded, we fetch it again. This way we aren't super dependant on
            // JWT and can plug in something else.
            const axiosInstance = axios.create(base);
            axiosInstance({
              url: "/user/",
              method: "get",
              params: {},
            }).then((response) => {
              this.$store.commit("setAuthUser", {
                authUser: response.data,
                isAuthenticated: true,
              });
              this.$router.push({ name: "Home" });
            });
          })
          .catch((error) => {
            console.log(error);
            console.debug(error);
            console.dir(error);
          });
      },
    },
  };
</script>

<style lang="css"></style>
```

## Summary

There you have it, my quick-and-dirty notes on getting Django REST Framework, JWT, Axios, and Vue.js to play nice together. Be aware there are a two significant problems:

1. I'm not happy about using local storage, especially with JWT. In fact, my good friend Randall Degges has written about the [problems of JWT](https://developer.okta.com/blog/2017/08/17/why-jwts-suck-as-session-tokens).
2. I don't cover logging out. ;)

Credits:

- [Melvin Koh's blog post on the subject](https://hackernoon.com/jwt-authentication-in-vue-js-and-django-rest-framework-part-1-c40c5c0d4f6e)
- Too many Stackoverflow and Github issues to list here. :P
