import tkinter as tk
from tkinter import PhotoImage
import nltk
from textblob import TextBlob
from newspaper import Article


def summarise():
    url = utext.get('1.0', "end").strip()

    article = Article(url)

    article.download()
    article.parse()

    article.nlp()

    # Set state to normal to enable editing
    title.config(state='normal')
    author.config(state='normal')
    keywords.config(state='normal')
    pub_date.config(state='normal')
    summary.config(state='normal')
    sentiment.config(state='normal')

    title.delete('1.0', "end")
    title.insert('1.0', article.title)

    author.delete('1.0', "end")
    # To prevent the code from breaking.
    # If author is not mentioned in the HTML, return 'No authors mentioned' instead of leaving a blank space
    author.insert(
        '1.0', f'{article.authors if article.authors else "No authors mentioned"}')

    # To prevent the code from breaking.
    # If keywords are not mentioned in the HTML (rare case), return 'No keywords mentioned' instead of leaving a blank space
    keywords.delete('1.0', "end")
    keywords.insert(
        '1.0', f'{article.keywords if article.keywords else "No keywords mentioned"}')

    pub_date.delete('1.0', "end")
    # To prevent the code from breaking.
    # If publishing date is not mentioned in the HTML, return 'No date of publishing mentioned' instead of leaving a blank space
    pub_date.insert(
        '1.0', f'{article.publish_date if article.publish_date else "No date of publishing mentioned"}')

    summary.delete('1.0', "end")
    summary.insert('1.0', article.summary)

    analysis = TextBlob(article.text)
    sentiment.delete('1.0', "end")
    sentiment.insert(
        '1.0', f'Polarity: {analysis.polarity}, Sentiment: {"positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral"}')

    # Set state to disabled to disable user input
    title.config(state='disabled')
    author.config(state='disabled')
    keywords.config(state='normal')
    pub_date.config(state='disabled')
    summary.config(state='disabled')
    sentiment.config(state='disabled')


# Widgets

# Root color variables
bg_color = '#170A24'
fg_color = '#FFF'

# Root (main window styling)
root = tk.Tk()
root.title('News Summariser')
root.geometry('1000x650')
root.config(bg=bg_color, pady=10, padx=10)
photo = PhotoImage(file="./news.png")
root.iconphoto(False, photo)

# URL label
ulabel = tk.Label(root, text="URL of the news article")
ulabel.config(bg=bg_color, fg=fg_color)
ulabel.pack()

# URL text box
utext = tk.Text(root, height=1, width=100)
utext.config(bg=fg_color)
utext.pack()

# Title label
tlabel = tk.Label(root, text="Title")
tlabel.config(bg=bg_color, fg=fg_color)
tlabel.pack()

# Title text box
title = tk.Text(root, height=1, width=100)
title.config(state='disabled', bg=fg_color)
title.pack()

# Author label
alabel = tk.Label(root, text="Author")
alabel.config(bg=bg_color, fg=fg_color)
alabel.pack()

# Author text box
author = tk.Text(root, height=1, width=100)
author.config(state='disabled', bg=fg_color)
author.pack()

# Keywords label
klabel = tk.Label(root, text="Keywords")
klabel.config(bg=bg_color, fg=fg_color)
klabel.pack()

# Keywords text box
keywords = tk.Text(root, height=2, width=100)
keywords.config(state='disabled', bg=fg_color)
keywords.pack()

# Published date label
publabel = tk.Label(root, text="Publication Date")
publabel.config(bg=bg_color, fg=fg_color)
publabel.pack()

# Published date text box
pub_date = tk.Text(root, height=1, width=100)
pub_date.config(state='disabled', bg=fg_color)
pub_date.pack()

# Summary label
slabel = tk.Label(root, text="Summary")
slabel.config(bg=bg_color, fg=fg_color)
slabel.pack()

# Summary text box
summary = tk.Text(root, height=15, width=100)
summary.config(state='disabled', bg=fg_color, wrap='word')
summary.pack()

# Sentiment label
sentlabel = tk.Label(root, text="Sentiment Analysis")
sentlabel.config(bg=bg_color, fg=fg_color)
sentlabel.pack()

# Sentiment text box
sentiment = tk.Text(root, height=1, width=100)
sentiment.config(state='disabled', bg=fg_color)
sentiment.pack()

blank = tk.Label(root, bg=bg_color)
blank.pack()

# Button

btn = tk.Button(root, text="Summarise",
                command=summarise, relief='ridge', bg='#FFF', padx=3, pady=3)
btn.pack()

root.mainloop()
