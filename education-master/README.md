# Thinkful Unit 3.3

# Do Wealthier Countries Provide Better Education?

* edu_pop.py - uses lxml.html and scraperwiki packages to pull education life span data from a UN website, and populates education.db with this data
* edu_profile.py - simple profiling of the education data
* gdp_pop.py - pulls gdp data from a csv file and populates gdp table in education.db
* education.py - pulls data from edu_life and gdp tables in education.db and compares ave_yrs vs gdp (log(mean(gdp)))
