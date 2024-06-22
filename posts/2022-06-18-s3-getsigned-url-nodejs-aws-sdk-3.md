---
date: "2022-06-18T22:20:50.52Z"
published: true
tags:
  - nodejs
  - javascript
  - reference
  - howto
  - TIL
time_to_read: 10
title: Getting s3 pre-signed URLS using the Node.js AWS SDK v3
description: An easy-to-find copy/pastable reference for creating pre-signed URLs for getting of files using the Node.js AWS SDK v3.
image: /logos/til-1.png
twitter_image: /logos/til-1.png
---

An easy-to-find copy/pastable reference for creating pre-signed URLs for getting of files using the Node.js AWS SDK v3.

# Background

Maybe there's a reference in the docs that provides an easy-to-use documentation of the AWS SDK v3 method for creating pre-signed URLs using Node (or TypeScript). Alas, after 45 minutes of googling, stack overflowing, and other searching I couldn't find it. Yes, [the docs had examples](https://aws.amazon.com/blogs/developer/generate-presigned-url-modular-aws-sdk-javascript), but they weren't copy/pastable for lazy/productive coders like myself. Perhaps I need to improve my search skills? I managed to solve it, but that took more effort than I expected.

For what it is worth, I hope the maintainers of the Node.js AWS SDK v3 add a copy/pastable version somewhere more obvious. The official docs will show up in searches before this article.

In any case, I finally dug in and figured it out. So I can find it again in the future, I'm posting it here.

# Install Dependencies

```bash
yarn add @aws-sdk/s3-request-presigner
yarn add @aws-sdk/client-s3
```

# Create Utility Function

I encapsulated my solution in a function in `s3FileFetch.js` so I could use it across a project:

```javascript
import { getSignedUrl } from "@aws-sdk/s3-request-presigner";
import { S3Client, GetObjectCommand } from "@aws-sdk/client-s3";

// Create the config obj with credentials
// Always use environment variables or config files
// Don't hardcode your keys into code
const config = {
  credentials: {
    accessKeyId: process.env.AWS_ACCESS_KEY_ID,
    secretAccessKey: process.env.AWS_SECRET_ACCESS_KEY,
  },
  region: "us-west-2",
};
// Instantiate a new s3 client
const client = new S3Client(config);

async function getSignedFileUrl(fileName, bucket, expiresIn) {
  // Instantiate the GetObject command,
  // a.k.a. specific the bucket and key
  const command = new GetObjectCommand({
    Bucket: bucket,
    Key: fileName,
  });

  // await the signed URL and return it
  return await getSignedUrl(client, command, { expiresIn });
}

export default getSignedFileUrl;
```

# Usage

```javascript
import getFileUrl from "/lib/s3FileFetch";

async function returnThumbnail(thumbnail_key) {
  return await getFileUrl(thumbnail_key, "my_bucket", 3600);
}
```

# Any Suggestions?

This works but I'm certain it can be improved. If you have any suggestions on how to do this action better, let me know in social media or email!

# Updates

- 2022-06-19: Moved configuration and instantiation of `s3` object out of the function thanks to a suggestion by [Jake Patrick](https://github.com/defy93).
