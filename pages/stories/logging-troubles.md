---
title: Logging Troubles
author: Daniel Roy Greenfeld
date: "2018-06-30"
---

The guard opened the back doors of the van to let Daniel and Audrey out. "We're here," he said. "Welcome to the Plats." Then he shut the doors and drove off.

Audrey was crying. "We don't deserve this," she said. "All this because we forgot to remove a `console.log()` statement from one little page. It's not fair."

Daniel put his arm around her. "Coding style guidelines are the law around here," he said. "Remember back in our Python days when I would reject developers from the team for not following PEP8? JavaScript is no different."

"What do we do now?" Audrey said. "We have nothing, not even food or water. It's cold and I'm hungry."

"Let's scope out the place and figure out where we are," Daniel said. "See that plateau up there? If we can find a way to get up there, we'll get a good view of the area."

Audrey nodded. Daniel led her to the base of the cliff. "Let's walk up this wall," he said. "Our antigravity shoes should cling to it just fine." He stepped onto the wall, leading Audrey upward. Soon they were walking sideways, their bodies parallel with the ground.

Suddenly Audrey slipped. Before she could fall, Daniel grabbed her just in time. Her watch beeped, and she looked at her wrist. Hundreds of lines of debugging printouts scrolled by.

"Looks like debug logging," Audrey said, her legs dangling down as Daniel held her. "Out here I guess they don't remove all the logging statements. There's just so much information. I can't make any sense of it."

"Logging as punishment," Daniel said. "Heh."

"It was my fault for disabling my ESLint pre-commit hook," Audrey said. "You had nothing to do with it. You shouldn't even be here."

"I belong wherever you are," Daniel said.

"I'm never using logging again," Audrey said. "From now on, I'm just going to debug my code by staring at it until I find each error."

"I'll help you," Daniel said. "I'll stare at your code with you. We'll pair program. But right now we need to finish getting up this wall. Let's go."

Daniel bent down to check Audrey's boots. They were gripping the wall tightly again. He stood up and led her up the side of the plateau. An hour later, they reached the top and climbed onto the flat ground.

"Look at the view," Audrey said. "It's incredible. We're above everything in sight."

The plateau towered high above the landscape. Below them were hundreds of plateaus of various sizes. At the bottom below those plateaus was deep blue ocean. A winding road with a gate cut through the ocean waters, elevated to the level of the lowest plateaus.

"There are pine trees up here with edible cones," Daniel said. "Look over there. See how the cones all point north? That means they're edible."

"Thank goodness we have food," Audrey said. "But what about water? I'm so thirsty. Even that ocean water is looking good right now."

"We'll find water," Daniel said. "It's a solvable problem. All we have to do is debug it. Which means we have to find the source code."

"Check your wristwatch," Audrey said. "If mine was printing logging statements, yours might have clues too."

Daniel squinted at his wrist. "All I see is configuration," he said. "YAML in every direction I scroll. Configuration isn't code."

Audrey looked at Daniel's wristwatch. "That's YAML with one-space indentation," she said. "They're really doing their best to torture us. I can't keep straight which lines match up with which."

"Let me take care of that part," Daniel said. "I'm good at that. I just use the cursor position numbers to keep track of things."

He scrolled around. Finally he found this line:

```yaml
- Water: "Not Enough"
```

"I got this!" Daniel exclaimed. "I just have to change the water setting to Enough!" He made a few gestures with his arms, wiggled his shoulders, flapped his elbows like a giant pigeon, and pursed his lips.

"You're amazing with that gestural interface," Audrey said.

Then the YAML changed:

```yaml
- Water: "Too Much"
```

"I think I went a bit overboard," Daniel said. "Oops."

The ocean below them began to churn. Waves grew larger and larger. The water level rose up over the lowest plateaus.

"Let me see," Audrey said, grabbing his wrist. "I know I really shouldn't do this, but I'm out of other ideas."

Audrey sneezed on Daniel's wristwatch display six times. Then the display changed to:

```js
console.log("Water setting:", env.water)
```

Daniel gasped. "We'll never get out of here if you log like that," he said.

"It's life or death," Audrey said. "Help me figure this out. Look for any setting in the `env.water` that we can use. Can you think of anything do with these three settings?

```javascript
let water = {
  amount: "Too Much",
  temperature: "cold",
  salinity: "salty"
}
```

"I can't think of anything," Daniel said in a glum voice. "Seeing how fast that ocean is coming, I think we're done for. If only we could more easily change a setting. Or even add a useful one."

"That's it!" Audrey said. "Water isn't a defined as a constant via `const`, but rather as a mutable via `let`. That means we can make any change to it we want. Let's just add a new setting just like so:

```javascript
water = {
  amount: "Too Much",
  temperature: "cold",
  salinity: "salty",
  drain: true
}
```

Audrey and Daniel breathed a sigh of relief as the ocean waters began to recede.

"I think coming here wasn't a curse, it was a blessing," Daniel said.

"I don't know about," Audrey said. "Making manual changes like this to a system is never the right approach. Maybe not today, or tomorrow, but some day this going to come back and bite us."

"Spoken like a true programmer," Daniel said in agreement.
