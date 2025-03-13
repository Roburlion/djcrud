# DjCrud - A Django Experiment in Progress

Welcome to `DjCrud`—a simple Django project where functionality comes first, and the setup is just a means to an end. This isn’t about perfection; it’s about building something that works, having fun, and figuring out the rest later. Expect a mix of chaos, progress, and maybe some funky features.

## What’s This About?
This is my playground for learning Django. I’m focusing on getting stuff done—building features first, then maybe adding some scaffolding or polish if I feel like it. Right now, it’s a work in progress, but it’s alive!

*(Note: I’ll add a specific description here once you tell me what the app does!)*

## Getting Started
Here’s how to fire this thing up. I’m using Windows (PowerShell), but adapt as needed for your setup. Folder structure? Still figuring that out—bear with me.

### Prerequisites
- Python 3.x (I’m using whatever `py` points to)
- A sense of adventure

### Setup
1. **Clone the repo** (if you’re reading this on GitHub):
   ```powershell
   git clone <your-repo-url>
   cd my_django_project
   ```

2. **Create and activate a virtual environment**:
   ```powershell
   py -m venv venv
   .\venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```powershell
   py -m pip install --upgrade pip
   pip install django
   ```

4. **Start the Django project** (if you’re starting fresh):
   ```powershell
   django-admin startproject djcrud
   cd djcrud
   ```

5. **Run the server**:
   ```powershell
   py manage.py runserver
   ```
   Open `http://127.0.0.1:8000/` in your browser. If you see something, we’re golden!

### Apps So Far
- `home`: The landing spot. Basic, but it’s there.
- `djfunky`: Something funky’s brewing here. *(Tell me more about this!)*

To add these apps:
```powershell
(venv) djcrud> py manage.py startapp home
(venv) djcrud> py manage.py startapp djfunky
```
*(Note: Don’t forget to add them to `INSTALLED_APPS` in `settings.py`!)*

## Development Approach
I’m building this iteratively:
1. **Functionality First**: Get something working (e.g., a CRUD feature).
2. **Scaffolding Later**: Maybe add templates or fancy setup stuff if I’m not burned out.
3. **Repeat**: More features, more fun.

The setup part was killing me, so I’m keeping it simple and diving into the good stuff. Check the code to see what’s cooking!

## Contributing
This is my mess for now, but if you want to jump in, feel free. Just don’t judge the folder structure too hard—I’m still experimenting.

## Troubleshooting
- Server won’t start? Check if `manage.py` is happy and your virtual env is active.
- Lost in the docs? Me too—try `django-admin --help` or hit up the [Django docs](https://docs.djangoproject.com/).

## Next Steps
- Build something useful (TBD based on your answers!).
- Maybe organize this chaos a bit.

Let’s keep the vibes high and the errors low. Happy coding!

# Change Log
## 20250310
What have we done!?

We've (Sr. Grok and I) put in some base template goodness!

Next stop: HTMX!

The goal is to change tbe button to use HTMX to update the table without a refresh.

Also want to limit the table to the 10 most recent presses.

## 20250310 - Later that evening
Holy fucking shit-sugary-goodness!!!  It's alive!!!

HTMX and DRY _partial_templates!

### Next steps
What's next?  The next things for this app is to think what the first things I will really need in the app.  For the Roll Tool, that has to be uploading a file.  I need to upload the aging file and then parse it with pandas.

Which comes first, the model or the upload, and where are these in relationship to the cart?

I guess the model would come first, and then pandas would populate the model.  Lets Grok it!

Here is my main query so far

[Grok on my app](https://grok.com/share/bGVnYWN5_005c0f86-c05a-453e-9014-61763834876a)

The way forward to the "Hello, World!" version of this.  Something very simple.  Like uploading a series of datetimes into my existing button log model/table.  Then I can slowly expand on this before I get into anything crazy.

## 20250312 @ 2am
The plan is to crate a new page, upload_button_page.html, with a dropzone and button to upload files.  Once I have the upload, I'll dump the contents into the db.

 - upload
 - validate
 - parse
 - upload
 -  - (I don't know what to do here, the goal is to manipulate and move as little data as possible.  Do I upload to a staging table and then use a sql query to write to the main table?  Do I figure out what and what not to upload in python?  If I did this, what data would I need to pull from the db to validate, and is the just going in circles?)

Dev plan
 - Create a new template
 - Add a dropzone
 - setup dropzone.js
 - do the stuff above

## 20250312 @ 3am
Upload page is up and running with a simple text placeholder.  What's next?  Add dropzone js and have a dummy place to upload a file.  Done, looks like shit, but it's there.

I can go one of two ways, I can make it look better, then wire it up, or I can wire it up and then make it look better.

I think I want to play a little.  Let me use one of those cards with the hover effect and then I'll wire it up.

What is the next step?
Put in a card.

Such a pain in the ass, all of this damn CSS.

## 20250312 @ 5am

Ok, I have the dropzone in /upload_button_page.  Now I want to dump the rows to the console.

## 20250312 @ 7am

I am now able to add rows to the buttonlog table by dropping in excel files!

## 20250313 @ 3am

The goal this morning is the be able to upload an aging file
 - Create a new page
 - New Model(s)
   - Write to a log model to keep track of uploads
 - New URL
 - New View








-------------------------------------------------------------------------------
-------------------------------------------------------------------------------
-------------------------------------------------------------------------------
# Original ReadMe Blather
This is a simple project.  Functionality first.  The problems that I have been running into is that I am too focused on the setup part, which is killing me.  I don't think it's bad, but I want to focus on some functionality first.  Focus on the building the thing.  Build some functionality, then add a scaffolding feature, then back to functionality.  Lets have fun with this.

# starting the project
I never quite know what is going on with the folder structure.  But I'm playing around with things.  Right now I'm in \my_django_project.

```powershell
> py -m venv venv
> .\venv\Scripts\activate
> py -m pip install --upgrade pip
> pip install django
> django-admin --version
> django-admin startproject djcrud
> cd .\djcrud\
> code .
> py manage.py runserver
```

```powershell
(venv) djcrud> py manage.py startapp home
(venv) djcrud> py manage.py startapp djfunky
(venv) djcrud> 
(venv) djcrud> 
(venv) djcrud> 
(venv) djcrud> 
```

