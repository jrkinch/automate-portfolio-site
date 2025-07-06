'''
    project testing portfolio projects page using playwright and pytest.
    
    Run all: python -m pytest -v
    Run only this section: python -m pytest -v -k test_portfolio_projects.py

    Notes:
    - different navbar vs sitemap:
        #get_by_role("list").get_by_role("link", name="Home") #navbar item
        #get_by_role("contentinfo").get_by_role("link", name="Home") #footer item
    - difference source code links:
        1) aka get_by_role("link", name="Source Code").first
        2) aka get_by_role("link", name="Source Code").nth(1)
        3) aka get_by_role("link", name="Source Code").nth(2)
        4) aka get_by_role("link", name="Source Code").nth(3)
'''
import pytest
from playwright.sync_api import Playwright, Page, expect
import re

#Menu NAVBAR
def test_menu_home_button(page: Page):
    page.goto("https://jrkinch.github.io/pages/projects.html#projects")
    
    page.get_by_role("list").get_by_role("link", name="Home").click()
    
    expect(page).to_have_title(re.compile("Welcome"))
    expect(page.get_by_role("heading", name="Passion For Quality.")).to_be_visible()
    expect(page).to_have_url("https://jrkinch.github.io/index.html#home")
    
def test_menu_projects_button(page: Page):
    page.goto("https://jrkinch.github.io/pages/projects.html#projects")
    
    page.get_by_role("list").get_by_role("link", name="Projects").click()
    
    expect(page).to_have_title(re.compile("Projects"))
    expect(page).to_have_url("https://jrkinch.github.io/pages/projects.html#projects")

def test_menu_about_button(page: Page):
    page.goto("https://jrkinch.github.io/pages/projects.html#projects")
    
    page.get_by_role("list").get_by_role("link", name="About").click()
    
    expect(page).to_have_title(re.compile("About"))
    expect(page.get_by_role("heading", name="More about me:")).to_be_visible()
    expect(page).to_have_url("https://jrkinch.github.io/pages/about.html#about")

def test_menu_contact_button(page: Page):
    page.goto("https://jrkinch.github.io/pages/projects.html#projects")
    
    page.get_by_role("list").get_by_role("link", name="Contact").click()
    
    expect(page).to_have_title(re.compile("Contact me"))
    expect(page.get_by_role("heading", name="Get in touch")).to_be_visible() 
    expect(page).to_have_url("https://jrkinch.github.io/pages/contact.html#contact")


#FOOTER
def test_footer_sitemap_home(page: Page):
    page.goto("https://jrkinch.github.io/pages/projects.html#projects")
    
    page.get_by_role("contentinfo").get_by_role("link", name="Home").click()
    
    expect(page).to_have_title(re.compile("Welcome"))
    expect(page.get_by_role("heading", name="Passion For Quality.")).to_be_visible()
    expect(page).to_have_url("https://jrkinch.github.io/index.html#home")
    
def test_footer_sitemap_projects(page: Page):
    page.goto("https://jrkinch.github.io/pages/projects.html#projects")
    
    page.get_by_role("contentinfo").get_by_role("link", name="Projects").click()
    
    expect(page).to_have_title(re.compile("Projects"))
    expect(page).to_have_url("https://jrkinch.github.io/pages/projects.html#projects")

def test_footer_sitemap_about(page: Page):
    page.goto("https://jrkinch.github.io/pages/projects.html#projects")
    
    page.get_by_role("contentinfo").get_by_role("link", name="About").click()
    
    expect(page).to_have_title(re.compile("About"))
    expect(page.get_by_role("heading", name="More about me:")).to_be_visible()
    expect(page).to_have_url("https://jrkinch.github.io/pages/about.html#about")

def test_footer_sitemap_contact(page: Page):
    page.goto("https://jrkinch.github.io/pages/projects.html#projects")
    
    page.get_by_role("contentinfo").get_by_role("link", name="Contact").click()
    
    expect(page).to_have_title(re.compile("Contact me"))
    expect(page.get_by_role("heading", name="Get in touch")).to_be_visible()
    expect(page).to_have_url("https://jrkinch.github.io/pages/contact.html#contact")

def test_footer_gh_image(page: Page):   
    page.goto("https://jrkinch.github.io/pages/projects.html#projects")
    
    expect(page.get_by_alt_text("GitHub")) 
    
def test_footer_goto_gh_link(page: Page):
    page.goto("https://jrkinch.github.io/pages/projects.html#projects")
    page.get_by_role("contentinfo").get_by_role("link", name="GitHub").click()#needed to resolve because of GitHub More Projects section.
    
    expect(page).to_have_title(re.compile("jrkinch"))
    expect(page).to_have_url("https://github.com/jrkinch")
   
def test_footer_li_image(page: Page):   
    page.goto("https://jrkinch.github.io/pages/projects.html#projects")
    
    expect(page.get_by_alt_text("LinkedIn"))  
    
def test_footer_goto_li_link(page: Page):
    page.goto("https://jrkinch.github.io/pages/projects.html#projects")
    page.get_by_role("link", name="LinkedIn").click()
    page.wait_for_timeout(5000)#linkedIn sometimes takes a while to load
    
    expect(page).to_have_title(re.compile(".*Jason Kinch | LinkedIn"))
    expect(page).to_have_url(re.compile(".*jason-kinch"))#needs regex search as url uses random auth redirect


#PAGE Contents
#PROJECT ONE
def test_page_project_one_title(page: Page):   
    page.goto("https://jrkinch.github.io/pages/projects.html#projects")
    
    expect(page.get_by_role("heading", name="Portfolio Site")).to_be_visible()
    
def test_page_project_one_image(page: Page):   
    page.goto("https://jrkinch.github.io/pages/projects.html#projects")
    
    expect(page.get_by_alt_text("Project One")).to_be_visible()
    
def test_page_project_one_description(page: Page):   
    page.goto("https://jrkinch.github.io/pages/projects.html#projects")
    
    expect(page.get_by_text("Project is this site.")).to_be_visible() 
    
def test_page_project_one_tech(page: Page):   
    page.goto("https://jrkinch.github.io/pages/projects.html#projects")
    
    expect(page.get_by_role("heading", name="HTML, CSS, JavaScript")).to_be_visible()
    
def test_page_project_one_source(page: Page):   
    page.goto("https://jrkinch.github.io/pages/projects.html#projects")
    
    page.get_by_role("link", name="Source Code").first.click()
    
    expect(page).to_have_url("https://github.com/jrkinch/jrkinch.github.io")
#PROJECT TWO
def test_page_project_two_title(page: Page):   
    page.goto("https://jrkinch.github.io/pages/projects.html#projects")
    
    expect(page.get_by_role("heading", name="Automate Portfolio")).to_be_visible()
    
def test_page_project_two_image(page: Page):   
    page.goto("https://jrkinch.github.io/pages/projects.html#projects")
    
    expect(page.get_by_alt_text("Project Two")).to_be_visible()
    
def test_page_project_two_description(page: Page):   
    page.goto("https://jrkinch.github.io/pages/projects.html#projects")
    
    expect(page.get_by_text("Project to automate portfolio web site.")).to_be_visible()
    
def test_page_project_two_tech(page: Page):   
    page.goto("https://jrkinch.github.io/pages/projects.html#projects")
    
    expect(page.get_by_role("heading", name="Playwright, Python")).to_be_visible()
    
def test_page_project_two_source(page: Page):   
    page.goto("https://jrkinch.github.io/pages/projects.html#projects")
    
    page.get_by_role("link", name="Source Code").nth(1).click()
    
    expect(page).to_have_url("https://github.com/jrkinch/automate-portfolio-site")
#PROJECT THREE
def test_page_project_three_title(page: Page):   
    page.goto("https://jrkinch.github.io/pages/projects.html#projects")
    
    expect(page.get_by_role("heading", name="Folder Cleanup")).to_be_visible()
    
def test_page_project_three_image(page: Page):   
    page.goto("https://jrkinch.github.io/pages/projects.html#projects")
    
    expect(page.get_by_alt_text("Project Three")).to_be_visible()
    
def test_page_project_three_description(page: Page):   
    page.goto("https://jrkinch.github.io/pages/projects.html#projects")
    
    expect(page.get_by_text("Project to organize specified folder.")).to_be_visible()
    
def test_page_project_three_tech(page: Page):   
    page.goto("https://jrkinch.github.io/pages/projects.html#projects")
    
    expect(page.get_by_role("heading", name="Python", exact=True)).to_be_visible()
    
def test_page_project_three_source(page: Page):   
    page.goto("https://jrkinch.github.io/pages/projects.html#projects")
    
    page.get_by_role("link", name="Source Code").nth(2).click()
    
    expect(page).to_have_url("https://github.com/jrkinch/folder-cleanup")
#PROJECT FOUR
def test_page_project_four_title(page: Page):   
    page.goto("https://jrkinch.github.io/pages/projects.html#projects")
    
    expect(page.get_by_role("heading", name="Jpad")).to_be_visible()
    
def test_page_project_four_image(page: Page):   
    page.goto("https://jrkinch.github.io/pages/projects.html#projects")
    
    expect(page.get_by_alt_text("Project Four")).to_be_visible() 
    
def test_page_project_four_description(page: Page):   
    page.goto("https://jrkinch.github.io/pages/projects.html#projects")
    
    expect(page.get_by_text("Simple text editor prototype that has tabs.")).to_be_visible() 
    
def test_page_project_four_tech(page: Page):   
    page.goto("https://jrkinch.github.io/pages/projects.html#projects")
    
    expect(page.get_by_role("heading", name="Java", exact=True)).to_be_visible()
    
def test_page_project_four_source(page: Page):   
    page.goto("https://jrkinch.github.io/pages/projects.html#projects")
    
    page.get_by_role("link", name="Source Code").nth(3).click()
    
    expect(page).to_have_url("https://github.com/jrkinch/jpad-text-editor")
#OTHER GITHUB PROJECTS
def test_page_project_others_title(page: Page):   
    page.goto("https://jrkinch.github.io/pages/projects.html#projects")
    
    expect(page.get_by_role("heading", name="More Projects")).to_be_visible()
    
def test_page_project_others_image(page: Page):   
    page.goto("https://jrkinch.github.io/pages/projects.html#projects")
    
    expect(page.get_by_alt_text("More projects at GitHub")).to_be_visible() 
    
def test_page_project_others_description(page: Page):   
    page.goto("https://jrkinch.github.io/pages/projects.html#projects")
    
    expect(page.get_by_text("Check out my other project repos.")).to_be_visible() 
    
def test_page_project_others_source(page: Page):   
    page.goto("https://jrkinch.github.io/pages/projects.html#projects")
    page.get_by_text("GitHub").click() 
    
    expect(page).to_have_url("https://github.com/jrkinch")