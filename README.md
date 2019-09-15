
![alt-text](https://images.unsplash.com/photo-1493972741200-51d407e0ee33?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1950&q=80)

Source: https://medium.com/data-science-library/amazing-data-science-publications-on-medium-17c5ba862774

## List of Top DS Publications
* Towards Data Science: https://towardsdatascience.com
* Learn Data Science: https://blog.exploratory.io
* Applied Data Science: https://medium.com/applied-data-science
* Center for Data Science: https://medium.com/center-for-data-science


## List of Top ML Publications
* Learning New Stuff: https://medium.com/learning-new-stuff
* Machine Learnings: https://machinelearnings.co/
* Machine Learning for Humans: https://medium.com/machine-learning-for-humans
* ML Review: https://medium.com/mlreview
* Open Machine Learning Course: https://medium.com/open-machine-learning-course
* metaflow-ai: https://blog.metaflow.fr/
* Inside Machine Learning: https://medium.com/inside-machine-learning

## Bot Description

Primarily, there are two bots working here and you have to run them sequentially in the following order:

### link_scrap 
Collects the links of the articles of the above publications. 

**Running the `link_scrap` bot will:**

Collect all the links of the articles and store them in a local mongo database.

  - **Database Name:** `mediumCrawl`
  - **Collection Name:** `mediumLinks`
  - **Document Format:** 

    ```js
    {
	"_id" : ObjectId("5d7df79048b3c66d77c86fe3"),
	"articleTitle" : "Guitar-Set, a New Dataset for Music Information Retrieval",
	"articleLink" : "https://medium.com/center-for-data-science/guitar-set-a-new-dataset-for-music-information-retrieval-41b7861a87d7?source=collection_archive---------0-----------------------"
}

### content_scrap
Collects the contents of the links aggregated via the `link_scrap` bot

**Running the `link_scrap` bot will:**

Collect the desired contents of the articles from the links (aggregated by `link_scrap` bot and stored inside `mediumLinks` collection ) and store them in a local mongo database.

  - **Database Name:** `mediumCrawl`
  - **Collection Name:** `mediumContents`
  - **Document Format:** 

    ```js
    {'articleTile': 'NYU researchers invent new real-time data analysis system for '
                'humanitarian agencies',
    'content': ['How can we tame the dragon', 'What is coming in future... '],
    'nameOfAuthor': 'NYU Center for Data Science',
    'nameOfPublication': 'Center for Data Science',
    'postingTime': '2018-01-24T15:19:52.202Z'}
    ```



### Run the Bots
* Create and activate a virtual environment, via

  ```
  $ python3 -m venv venv
  $ source venv/bin/activate
  ```

* Install the requirements via

  ```
  pip install -r requirements.txt
  ```

#### 1. `link_scrap`
To run the first bot,

  * Install `mongodb`

  * Run the local `mongo` server

  * `cd` to `link_scrap` directory

  * Run 
    ```
    $ scrapy crawl link_scrap
    ```
  * You should see a `links.jl` file in your current directory and the documents in `mediumLinks` collection inside `mediumCrawl` database

  * You can count the number of 
  documents saved in your local mongo database via running the following command in your `mongo shell`:
      ```
      > db.mediumLinks.countDocuments({})
      ```

#### 2. `content_scrap`
To run the second bot, 
  * Keep your `mongo` server running
  * `cd` to `content_scrap`
  * Run 
    ```
    $ scrapy crawl content_scrap
    ``` 
  * You should a `contents.jl` file in your current directory and the documents in `mediumContents` collection inside `mediumCrawl` database

  * You can count the number of documents saved in your local mongo database via running the following command in your `mongo shell`:
      ```
      > db.mediumContents.countDocuments({})
      ```
    
  * To see a sample document, run
      ```
      db.mediumContents.findOne()
      ```

## Issues

* Article title (collected by `link_scrap`) scraping is not perfect, there are a lot of null values for article title here and there (this is not a big deal since we are collecting the titles again while running the `content_scrap` bot ) 
