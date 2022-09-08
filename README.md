<h1 align="center">Foodive</h1>
<p align="center">
<img width="364" alt="Screen Shot 2022-09-06 at 8 54 44 PM" src="https://user-images.githubusercontent.com/92293363/188778379-1acef02a-e6be-4505-be9d-2e9d169aea1d.png">
</p>
<details>
<summary> Table of Contents</summary>
<ol>
<li>About the Project</li>
<ul>
<li> Built With </li>
</ul>
<li> Getting Started </li>
<ul>
<li> Prerequisites </li>
<li> Installation </li>
</ul>
<li> EndPoints </li>
<ul>
<li> Partner Repository</li>
</ul>
<ul>
<li> Contributors </li>
</ul>
<li> Thank you </li>
</ol>
</details>

## About the Project
Take the thinking out of picking a restaurant and use Foodive! Foodive is an application that allows you to click one button and it will randomly select a restaurant in your area. When the restaurant is selected, business details are provided such as rating, price and food category! Want a specific restaurant? Use the filters feature, where if you want a specific genre of food like mexican, click the button "mexican" and your one click away from getting a random mexican restaurant. This is a backend application which has a partner repo called fe-foodive(https://github.com/foodive/fe-foodive.git)  

### Built With
- ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
- ![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
- ![Heroku](https://img.shields.io/badge/Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white)
- ![CircleCi](https://img.shields.io/badge/circleci-343434?style=for-the-badge&logo=circleci&logoColor=white)
- ![Figma](https://img.shields.io/badge/Figma-F24E1E?style=for-the-badge&logo=figma&logoColor=white)
- ![Atom](https://img.shields.io/badge/Atom-66595C?style=for-the-badge&logo=Atom&logoColor=white)
- ![VSCode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white)
- ![Github](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)
- ![Love](http://ForTheBadge.com/images/badges/built-with-love.svg)


## Getting Started

### Prerequisites
- ![Python](https://img.shields.io/badge/pythonversion-v3.10.6-blue)
- ![Django](https://img.shields.io/badge/djangoversion-v4.1-blue)

### Installation
1. Get your API key from these websites
- Yelp Api - https://www.yelp.com/developers/documentation/v3

2. Clone the repo
`git@github.com:foodive/be-foodive-python.git`

3. Move into the file
`cd be-foodive-python`

4. Setup virtual environment
`python3 -m venv .venv`

5. Activate virtual environment
`. venv/bin/activate`

6. Install django packages
`pip install -r requirements.txt`

7. Create `.env` file in the root directory of the project and insert `YELP_API_KEY=YOUR API KEY`

8. Delete `.circleci` folder

9. Please clone foodive-fe repoistory to ensure full functionalilty of the application

9. Happy Hunting!

## End Points
#### Retrieve a random restaurant 
```
GET /restaurants/?location=denver&categories=mexican
```

```
{
"data": {
    "id": "null",
    "type": "restaurant_info",
    "attributes": {
        "name": "El Camino Community Tavern",
        "image_url": "https://s3-media4.fl.yelpcdn.com/bphoto/on-W4Ctj96UOMeM5phdphA/o.jpg",
        "categories": [
            "Mexican",
            "Bars",
            "Breakfast & Brunch"
            ],
        "rating": 4,
        "coordinates": {
            "latitude": 39.762136,
            "longitude": -105.03544
        },
        "price": "$$",
        "display_address": [
            "3628 W 32nd Ave",
            "Denver, CO 80211"
        ],
        "display_phone": "(720) 889-7946"
        }
    }
}
```

## Partner Repository
- https://github.com/foodive/fe-foodive
- **Heroku App Frontend**  = https://foodive.herokuapp.com/
- **Heroku App Backend** = https://foodive-be.herokuapp.com/

## Contributions
#### BackEnd Team
<p>📶 Luke Swenson:  Github: https://github.com/LukeSwenson06 Linkedin: https://www.linkedin.com/in/luke-swenson </p>
<p>🥟 Becky Nisttahuz:  Github: https://github.com/benistta Linkedin: https://www.linkedin.com/in/becky-nisttahuz/ </p>
<p>🪴 Jim Riddle:  Github: https://github.com/jimriddle1 Linkedin: https://www.linkedin.com/in/jim-riddle-b6718037/ </p>

#### FrontEnd Team
<p>🍲 Lourdes Benites:  Github: https://github.com/lourdesbnts Linkedin: https://www.linkedin.com/in/lourdesbenites/ </p>
<p>🔖 Kristy Nguyen:  Github: https://github.com/kpn678 Linkedin: https://www.linkedin.com/in/kristypnguyen/ </p>
<p>🌃 Dylan Duke:  Github: https://github.com/laytonmaes Linkedin: https://www.linkedin.com/in/dylan-duke-005756129/ </p>
<p>🎨 Grant X Beard:  Github: https://github.com/GrantXBeard Linkedin: https://www.linkedin.com/in/grant-x-beard/ </p>

# Thank You
