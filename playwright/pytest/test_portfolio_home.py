'''
    project testing portfolio home page using playwright and pytest.
    
    Run all: python -m pytest -v
    Run only this section: python -m pytest -v -k test_portfolio_home.py

    Notes:
    - different navbar vs sitemap:
        #get_by_role("list").get_by_role("link", name="Home") #navbar item
        #get_by_role("contentinfo").get_by_role("link", name="Home") #footer item
'''
import pytest
from playwright.sync_api import Playwright, Page, expect
import re

#Menu NAVBAR
def test_menu_home_button(page: Page):
    page.goto("https://jrkinch.github.io/")
    
    page.get_by_role("list").get_by_role("link", name="Home").click()
    
    expect(page).to_have_title(re.compile("Welcome"))
    expect(page.get_by_role("heading", name="Passion For Quality.")).to_be_visible()
    expect(page).to_have_url("https://jrkinch.github.io/index.html#home")
    
def test_menu_projects_button(page: Page):
    page.goto("https://jrkinch.github.io/")
    
    page.get_by_role("list").get_by_role("link", name="Projects").click()
    
    expect(page).to_have_title(re.compile("Projects"))
    expect(page).to_have_url("https://jrkinch.github.io/pages/projects.html#projects")

def test_menu_about_button(page: Page):
    page.goto("https://jrkinch.github.io/")
    
    page.get_by_role("list").get_by_role("link", name="About").click()
    
    expect(page).to_have_title(re.compile("About"))
    expect(page.get_by_role("heading", name="More about me:")).to_be_visible()
    expect(page).to_have_url("https://jrkinch.github.io/pages/about.html#about")

def test_menu_contact_button(page: Page):
    page.goto("https://jrkinch.github.io/")
    
    page.get_by_role("list").get_by_role("link", name="Contact").click()
    
    expect(page).to_have_title(re.compile("Contact me"))
    expect(page.get_by_role("heading", name="Get in touch")).to_be_visible() 
    expect(page).to_have_url("https://jrkinch.github.io/pages/contact.html#contact")


#FOOTER
def test_footer_sitemap_home(page: Page):
    page.goto("https://jrkinch.github.io/")
    
    page.get_by_role("contentinfo").get_by_role("link", name="Home").click()
    
    expect(page).to_have_title(re.compile("Welcome"))
    expect(page.get_by_role("heading", name="Passion For Quality.")).to_be_visible()
    expect(page).to_have_url("https://jrkinch.github.io/index.html#home")
    
def test_footer_sitemap_projects(page: Page):
    page.goto("https://jrkinch.github.io/")
    
    page.get_by_role("contentinfo").get_by_role("link", name="Projects").click()
    
    expect(page).to_have_title(re.compile("Projects"))
    expect(page).to_have_url("https://jrkinch.github.io/pages/projects.html#projects")

def test_footer_sitemap_about(page: Page):
    page.goto("https://jrkinch.github.io/")
    
    page.get_by_role("contentinfo").get_by_role("link", name="About").click()
    
    expect(page).to_have_title(re.compile("About"))
    expect(page.get_by_role("heading", name="More about me:")).to_be_visible()
    expect(page).to_have_url("https://jrkinch.github.io/pages/about.html#about")

def test_footer_sitemap_contact(page: Page):
    page.goto("https://jrkinch.github.io/")
    
    page.get_by_role("contentinfo").get_by_role("link", name="Contact").click()
    
    expect(page).to_have_title(re.compile("Contact me"))
    expect(page.get_by_role("heading", name="Get in touch")).to_be_visible()
    expect(page).to_have_url("https://jrkinch.github.io/pages/contact.html#contact")

def test_footer_gh_image(page: Page):   
    page.goto("https://jrkinch.github.io/")
    
    expect(page.get_by_alt_text("GitHub")) 
    
def test_footer_goto_gh_link(page: Page):
    page.goto("https://jrkinch.github.io/")
    page.get_by_role("link", name="GitHub").click()
    
    expect(page).to_have_title(re.compile("jrkinch"))
    expect(page).to_have_url("https://github.com/jrkinch")
   
def test_footer_li_image(page: Page):   
    page.goto("https://jrkinch.github.io/")
    
    expect(page.get_by_alt_text("LinkedIn"))  
    
def test_footer_goto_li_link(page: Page):
    page.goto("https://jrkinch.github.io/")
    page.get_by_role("link", name="LinkedIn").click()
    page.wait_for_timeout(5000)#linkedIn sometimes takes a while to load
    
    expect(page).to_have_title(re.compile(".*Jason Kinch | LinkedIn"))
    expect(page).to_have_url(re.compile(".*jason-kinch-84317960"))#needs regex search as url uses random auth redirect


#PAGE Contents
def test_page_has_title(page: Page):
    page.goto("https://jrkinch.github.io/")
    
    expect(page).to_have_title(re.compile("Welcome"))
    
def test_page_has_header(page: Page):   
    page.goto("https://jrkinch.github.io/")
    
    expect(page.get_by_role("heading", name="Passion for Quality.")).to_be_visible()

def test_page_has_greeting(page: Page):   
    page.goto("https://jrkinch.github.io/")
    
    expect(page.get_by_text("Hi, I'm Jason.")).to_be_visible()   
    
def test_page_has_intro(page: Page):   
    page.goto("https://jrkinch.github.io/")
    
    expect(page.get_by_text("I'm a passionate Software Quality Assurance Engineer who also develops tools and solutions.")).to_be_visible()      
    
def test_page_has_image(page: Page):   
    page.goto("https://jrkinch.github.io/")
    
    expect(page.get_by_alt_text("portrait image")).to_be_visible()   