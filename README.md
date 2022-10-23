# Template of a Django project serving markdown files

Source code relative to my [blog post](https://blog.kenshuri.com/posts/002_render_md_with_tailwind_typography.md) about rendering md file in Django.

## Set-up the project

To set-up the project from scratch, run the following commands in your terminal.

```shell
git clone https://github.com/kenshuri/render_md_with_tailwind_typography.git
cd render_md_with_tailwind_typography
python -m virtualenv venv
pip install -r requirements.txt
cd jstoolchains
npm install
```

You're good to go my friend!

## Start your project 

To see your project in action, open 2 terminals.

In the first terminal run:
```shell
cd render_md_with_tailwind_typography
cd jstoolchains
npm run tailwind-watch
```

In the second terminal run:
```
cd render_md_with_tailwind_typography
python manage.py runserver
```

As prompted, open the page http://127.0.0.1:8000/ and enjoy 🚀

Note that changes in your html template `blogApp\templates\blogApp\index.html` automatically updates what you see in your browser.


