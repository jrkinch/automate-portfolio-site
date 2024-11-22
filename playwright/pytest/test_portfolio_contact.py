'''
    project testing portfolio contact page using playwright and pytest.
    
    Run all: python -m pytest -v
    Run only this section: python -m pytest -v -k test_portfolio_contact.py

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
    page.goto("https://jrkinch.github.io/pages/contact.html#contact")
    
    page.get_by_role("list").get_by_role("link", name="Home").click()
    
    expect(page).to_have_title(re.compile("Welcome"))
    expect(page.get_by_role("heading", name="Passion For Quality.")).to_be_visible()
    expect(page).to_have_url("https://jrkinch.github.io/index.html#home")
    
def test_menu_projects_button(page: Page):
    page.goto("https://jrkinch.github.io/pages/contact.html#contact")
    
    page.get_by_role("list").get_by_role("link", name="Projects").click()
    
    expect(page).to_have_title(re.compile("Projects"))
    expect(page).to_have_url("https://jrkinch.github.io/pages/projects.html#projects")

def test_menu_about_button(page: Page):
    page.goto("https://jrkinch.github.io/pages/contact.html#contact")
    
    page.get_by_role("list").get_by_role("link", name="About").click()
    
    expect(page).to_have_title(re.compile("About"))
    expect(page.get_by_role("heading", name="More about me:")).to_be_visible()
    expect(page).to_have_url("https://jrkinch.github.io/pages/about.html#about")

def test_menu_contact_button(page: Page):
    page.goto("https://jrkinch.github.io/pages/contact.html#contact")
    
    page.get_by_role("list").get_by_role("link", name="Contact").click()
    
    expect(page).to_have_title(re.compile("Contact me"))
    expect(page.get_by_role("heading", name="Get in touch")).to_be_visible() 
    expect(page).to_have_url("https://jrkinch.github.io/pages/contact.html#contact")


#FOOTER
def test_footer_sitemap_home(page: Page):
    page.goto("https://jrkinch.github.io/pages/contact.html#contact")
    
    page.get_by_role("contentinfo").get_by_role("link", name="Home").click()
    
    expect(page).to_have_title(re.compile("Welcome"))
    expect(page.get_by_role("heading", name="Passion For Quality.")).to_be_visible()
    expect(page).to_have_url("https://jrkinch.github.io/index.html#home")
    
def test_footer_sitemap_projects(page: Page):
    page.goto("https://jrkinch.github.io/pages/contact.html#contact")
    
    page.get_by_role("contentinfo").get_by_role("link", name="Projects").click()
    
    expect(page).to_have_title(re.compile("Projects"))
    expect(page).to_have_url("https://jrkinch.github.io/pages/projects.html#projects")

def test_footer_sitemap_about(page: Page):
    page.goto("https://jrkinch.github.io/pages/contact.html#contact")
    
    page.get_by_role("contentinfo").get_by_role("link", name="About").click()
    
    expect(page).to_have_title(re.compile("About"))
    expect(page.get_by_role("heading", name="More about me:")).to_be_visible()
    expect(page).to_have_url("https://jrkinch.github.io/pages/about.html#about")

def test_footer_sitemap_contact(page: Page):
    page.goto("https://jrkinch.github.io/pages/contact.html#contact")
    
    page.get_by_role("contentinfo").get_by_role("link", name="Contact").click()
    
    expect(page).to_have_title(re.compile("Contact me"))
    expect(page.get_by_role("heading", name="Get in touch")).to_be_visible()
    expect(page).to_have_url("https://jrkinch.github.io/pages/contact.html#contact")

def test_footer_gh_image(page: Page):   
    page.goto("https://jrkinch.github.io/pages/contact.html#contact")
    
    expect(page.get_by_alt_text("GitHub")) 
    
def test_footer_goto_gh_link(page: Page):
    page.goto("https://jrkinch.github.io/pages/contact.html#contact")
    page.get_by_role("link", name="GitHub").click()
    
    expect(page).to_have_title(re.compile("jrkinch"))
    expect(page).to_have_url("https://github.com/jrkinch")
   
def test_footer_li_image(page: Page):   
    page.goto("https://jrkinch.github.io/pages/contact.html#contact")
    
    expect(page.get_by_alt_text("LinkedIn"))  
    
def test_footer_goto_li_link(page: Page):
    page.goto("https://jrkinch.github.io/pages/contact.html#contact")
    page.get_by_role("link", name="LinkedIn").click()
    page.wait_for_timeout(5000)#linkedIn sometimes takes a while to load
    
    expect(page).to_have_title(re.compile(".*Jason Kinch | LinkedIn"))
    expect(page).to_have_url(re.compile(".*jason-kinch-84317960"))#needs regex search as url uses random auth redirect


#PAGE Contents
def test_page_contact_title(page: Page):   
    page.goto("https://jrkinch.github.io/pages/contact.html#contact")
    
    expect(page.get_by_role("heading", name="Get in Touch")).to_be_visible()
    
def test_page_contact_name_field_check(page: Page):   
    page.goto("https://jrkinch.github.io/pages/contact.html#contact")
    
    expect(page.get_by_role("textbox", name="Your Name")).to_be_visible()

def test_page_contact_email_field_check(page: Page):   
    page.goto("https://jrkinch.github.io/pages/contact.html#contact")
    
    expect(page.get_by_role("textbox", name="Your Email")).to_be_visible()

def test_page_contact_subject_field_check(page: Page):   
    page.goto("https://jrkinch.github.io/pages/contact.html#contact")
    
    expect(page.get_by_role("textbox", name="Subject")).to_be_visible()

def test_page_contact_message_field_check(page: Page):   
    page.goto("https://jrkinch.github.io/pages/contact.html#contact")
    
    expect(page.get_by_role("textbox", name="Your Message")).to_be_visible()

def test_page_contact_submit_button_check(page: Page):   
    page.goto("https://jrkinch.github.io/pages/contact.html#contact")
    
    expect(page.get_by_role("button", name="Submit")).to_be_visible()
    expect(page.get_by_alt_text("send icon")).to_be_visible()
    
def test_page_contact_image(page: Page):   
    page.goto("https://jrkinch.github.io/pages/contact.html#contact")
    
    expect(page.get_by_alt_text("contact")).to_be_visible()

def test_page_contact_send_info(page: Page):   
    page.goto("https://jrkinch.github.io/pages/contact.html#contact")
    page.get_by_placeholder("Your Name").click()
    page.get_by_placeholder("Your Name").fill("Tester")
    page.get_by_placeholder("Your Email").click()
    page.get_by_placeholder("Your Email").fill("Tester@gmail.com")
    page.get_by_placeholder("Subject").click()
    page.get_by_placeholder("Subject").fill("Playwright Automation Test")
    page.get_by_placeholder("Your Message").click()
    page.get_by_placeholder("Your Message").fill("This was generated using the playwright and pytest automation tests.")
    page.get_by_role("button", name="Submit").click()
    
    page.wait_for_timeout(5000)#needed for sumbit to process
    expect(page.get_by_role("heading", name="Submission Confirmed."))
    expect(page.get_by_role("heading", name="Thank you for reaching out to me."))