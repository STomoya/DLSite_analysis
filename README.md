
# DLSite_analysis

Analysis on works selling at [DLSite.com](https://dlsite.com/).

Visit the [Github Pages](https://stomoya.github.io/DLSite_analysis/)
to see it moving.

## Github Pages

The code for visualization is written by:

- [Vue.js](https://vuejs.org/index.html)  
- [Chart.js](https://www.chartjs.org/)  
- [Bootstrap4](https://getbootstrap.com/)  

## For Developers

I am using Docker to run my python codes.  
If anyone, I think no-one will but, reproduce my work, it is easy.

### Requirement

- Docker
- docker-compose

And also network enviornment, because the code scrapes information from DLsite.  
If your network enviornment is super fast, I recommend to add intervals between scraping a page.

### Usage

  Download repository, build, up, and step into container:

  ```console
    $ git clone https://github.com/STomoya/DLSite_analysis.git
    $ cd DLSite_analysis/docker
    $ docker-compose build
    $ docker-compose up -d
    $ docker-compose exec dlsite_analysis bash
  ```

  Then in the container:

  ```console
    # make setup
  ```

  I believe This command will take a while to complete.  
  If something happens and stops, rerun the command.  

  After this finishes, access the index.html with your browser.  
  I believe this will do...

## Author

[Tomoya Sawada](https://github.com/STomoya/)
