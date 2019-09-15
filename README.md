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
    ```

### content_scrap
Collects the contents of the links aggregated via the `link_scrap` bot

* 


### Run the Bots

1. `link_scrap`:
To run the first bot,
    * Install mongodb
    * Run the local mongo server
    * `cd` to `link_scrap` directory
    * Run 
      ```
      $ scrapy crawl links
      ```
    * You should see a `links.json` file in your current directory and the documents in `mediumLinks` collection inside `mediumCrawl` database
    * You can count the number of documents saved in your local mongo database via running the following command in your `mongo shell`:
        ```
        > db.mediumLinks.countDocuments({})
        ```
