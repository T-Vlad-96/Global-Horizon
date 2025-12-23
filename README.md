![logo of the project](https://media.istockphoto.com/id/929047972/vector/world-news-flat-vector-icon-news-symbol-logo-illustration-business-concept-simple-flat.jpg?s=612x612&w=0&k=20&c=5jpcJ7xejjFa2qKCzeOXKJGeUl7KZi9qoojZj1Kq_po=)

# Global Horizon
### A website where redactors can register their profiles and publish newspapers (articles) on any topic under their name.
## Technologies stack
### Built with Python, Django Framework with help of Bootstrap5 and Crispy forms for better UX

## Developing
python3 must be already installed
- git clone https://github.com/T-Vlad-96/Global-Horizon.git
- cd Global-Horizon
- python3 -m venv venv
- source venv/bin/activate
- pip install -r requirements.txt
- python manage.py runserver

## Features
- Ability of creating, editing, deleting Topics, Redactors, Newspapers
- Every author (Redactor) has own profile with personal information, contact data and experience info.
- Newspapers may have several topics and authors. 
- Search functionality lets user quicly to find newspapers by it's title, topics by it's name and redactor by it's username
- Convenient navigation panel allows users quickly switch between sections of the website.

## Reflection
This project helped me better understand how to develop websites with good UX design. I learned more about Bootstrap and Crispy Forms.
I consolidated some of my knowledge regarding the back-end, such as Django user authentication system and Django forms.

### user with admin status to check the website functionality
- **login:** test_user
- **password:** TestPass1234
