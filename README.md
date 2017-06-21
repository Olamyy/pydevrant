# pydevRant

[pypi-image]: https://img.shields.io/badge/npm-v0.0.5-blue.svg

Unofficial Python wrapper for the **public** [devRant](https://www.devrant.io/) API.

![devRant](https://raw.githubusercontent.com/danillouz/devrant/master/devrant.png "devRant")

## Requirements
`requests`

## Installation
`pip install pydevrant`

This library exposes methods to fetch rants and users from
devRant.

## devRant Display Requirements
When displaying the contents of a rant fetched from the
[devRant](https://www.devrant.io/) API, it is **required**
to credit the author of a rant by displaying their devRant
username.


## Methods
Import the library by running:
`from pydevrant import devrant`

After requiring the module, the following methods can be
used:

### devrant.get_rant(id)
Retrieve a single rant from devRant. Use this method to retrieve a rant
with its full text and comments by passing the rant id. For example `43511`.

The method returns a [Full Rant Object](#rant-object-full).

```python

from pydevrant import devrant

rants = devrant.get_rants()
rant = devrant.get_rant('43511')
user = devrant.get_user('dfox')
user_profile = devrant.get_user_profile(user['user_id'])

```


### devrant.get_rants(options)
Retrieve rants from devRant.

By providing an options Object as an argument, it's possible
to sort by `algo`, `recent` and `top` rants. As well as
limiting and skipping the amount of rants to be fetched.

The method returns a  [Simple Rant Objects](#rant-object-simple).

###### Options
| OPTIONS KEY | TYPE | DESCRIPTION |
| --- | --- | --- | --- |
| sort  | String  | **Optional**. The type of rants to be fetched. Must be `algo`, `recent` or `top`. When omitted, it defaults to `algo`. |
| limit | Number | **Optional**. The amount of rants to be fetched. When omitted, it defaults to `50`. |
| skip | Number | **Optional**. The amount of rants to be skipped. When omitted, it defaults to `0`. |


### devrant.search_rants(term)
Retrieve rants from devRant that match a specific search
term.

The returned rants are [Simple Rant Objects](#rant-object-simple).


### dev.get_user_profile(username)
Retrieve the profile of a devRant user by username.

The retrieved profile is a [Profile Object](#profile-object).


## Rant Object Simple
```json
{
  "id": 43511,
  "text": "when people think you know everything...",
  "num_upvotes": 38,
  "num_downvotes": 1,
  "score": 37,
  "created_time": 1464610498,
  "attached_image": {
    "url": "https://d1fvlyhrbsf219.cloudfront.net/devrant/rant/r_43511_uQDW4.jpg",
    "width": 600,
    "height": 300
  },
  "num_comments": 5,
  "tags": [ ],
  "vote_state": 0,
  "user_id": 15601,
  "user_username": "Mung00se",
  "user_score": 272
}
```

## Rant Object Full
```json
{
  "rant": {
    "id": 43511,
    "text": "when people think you know everything...",
    "num_upvotes": 39,
    "num_downvotes": 1,
    "score": 38,
    "created_time": 1464610498,
    "attached_image": {
      "url": "https://d1fvlyhrbsf219.cloudfront.net/devrant/rant/r_43511_uQDW4.jpg",
      "width": 600,
      "height": 300
    },
    "num_comments": 5,
    "tags": [ ],
    "vote_state": 0,
    "user_id": 15601,
    "user_username": "Mung00se",
    "user_score": 273
  },
  "comments": [
    {
      "id": 43529,
      "rant_id": 43511,
      "body": "But at some point we all do it.",
      "num_upvotes": 2,
      "num_downvotes": 0,
      "score": 2,
      "created_time": 1464611516,
      "vote_state": 0,
      "user_id": 505,
      "user_username": "Jumpshot44",
      "user_score": 2233
    }
  ],
  "success": true
}
```

## Profile Object
```json
{
  "username": "danillouz",
  "score": 207,
  "about": "I spend too much time tweaking my terminal and color schemes..",
  "location": "The Netherlands",
  "created_time": 1463432703,
  "skills": "Node.js, JavaScript, mongoDB, GraphQL, ObjectiveC, Go",
  "github": "danillouz",
  "content": {
    "content": {
      "rants": [
        {
          "id": 38898,
          "text": "Me and my team are working on a system where we depend on a component that was built by a different dev team and hasn't been integration tested yet, because it's that new. This is how it's going..",
          "num_upvotes": 35,
          "num_downvotes": 0,
          "score": 35,
          "created_time": 1464211080,
          "attached_image": {
            "url": "https://d1fvlyhrbsf219.cloudfront.net/devrant/rant/r_38898_Z93E9.gif",
            "width": 380,
            "height": 230
          },
          "num_comments": 2,
          "tags": [
            "teams",
            "integration-testing",
            "dependencies"
          ],
          "vote_state": 0,
          "user_id": 27942,
          "user_username": "danillouz",
          "user_score": 207
        }
      ],
      "upvoted": [
        {
          "id": 42586,
          "text": "My office desk",
          "num_upvotes": 65,
          "num_downvotes": 0,
          "score": 65,
          "created_time": 1464530939,
          "attached_image": {
            "url": "https://d1fvlyhrbsf219.cloudfront.net/devrant/rant/r_42586_9jWtu.jpg",
            "width": 800,
            "height": 600
          },
          "num_comments": 18,
          "tags": [
            "mydesk"
          ],
          "vote_state": 0,
          "user_id": 13541,
          "user_username": "dvlpr",
          "user_score": 104
        }
      ],
      "comments": [
        {
          "id": 41422,
          "rant_id": 41065,
          "body": "@xroad Hodor",
          "num_upvotes": 3,
          "num_downvotes": 0,
          "score": 3,
          "created_time": 1464425475,
          "vote_state": 0,
          "user_id": 27942,
          "user_username": "danillouz",
          "user_score": 207
        }
      ]
    },
    "counts": {
      "rants": 5,
      "upvoted": 37,
      "comments": 16
    }
  }
}
```
