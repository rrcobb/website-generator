# Website Generator
Not everyone has the time to learn HTML and CSS. Still, they should still have the power to make websites. Let's create a tool with python that will generate HTML!

What is a website generator? Well, it should generate websites, of course! As we've learned, websites are nothing but text documents written in HTML. HTML describes the content that appears in the browser and links to other resources, such as CSS and Javascript, which define the style and action of the page.

Write your functions in generator.py, then run `$ python generator_test.py` to check whether you've got it working. The tests are pretty specific - they don't leave much room for error.

(If you've installed nose and rednose, you can run the tests with `$nosetests --rednose`)
## The first step - paragraphs
We want to write good, maintainable code. That means breaking down our generator into smaller functions, and implementing them one by one.

First, let's write a function that turns a string of text into an HTML paragraph. Name your function create_paragraph(). It should take a string argument like this:
```python
"I've heard there are troubles of more than one kind; some come from ahead, and some come from behind. But I've brought a big bat. I'm all ready, you see; now my troubles are going to have troubles with me!"
```
And return that string, wrapped in `<p>` and `</p>` tags:
```python
"<p>I've heard there are troubles of more than one kind; some come from ahead, and some come from behind. But I've brought a big bat. I'm all ready, you see; now my troubles are going to have troubles with me!</p>"
```
Run the tests, and the first test should pass.

## Headers
Next, add a function to create a header. Call it create_header. It should accept a string that will be the header, and an integer between 1 and 6 for the level of header. It should return a string with an HTML header of the specified level.

Someone could call your function like this:
```python
create_header("Fox In Socks",2)
```
And they should get back:
```python
"<h2>Fox In Socks</h2>"
```
If they pass in a number that isn't between 1 and 6, return the string back without changing it:
```python
create_header("More than 6",7)
>>> "More than 6"
```
Make the test pass!

## Links
Users of your tool need their anchor tags. They just gotta link to that YouTube video! This time, they'll pass in the content that goes in the tag as well as the destination of the link, both as strings.

A call would look like:
```python
create_link("Check out this Dr. Seuss Website","http://www.seussville.com/")
```
It should return:
```python
"<a href='http://www.seussville.com/'>Check out this Dr. Seuss Website</a>"
```
Another function, another test to pass!

## Images
Beautiful websites need images. They're our favorite parts of the web! Let's add a function for image tags. Images don't have any content inside the element - instead, they have a source. Optionally, they should have an alt attribute, defining the text that should appear if the image doesn't load, or for those using screen readers.

Both of the following calls should work:
```python
create_image('http://www.hdwallpapersimages.com/wp-content/uploads/2014/01/Winter-Tiger-Wild-Cat-Images.jpg')
create_image('http://www.hdwallpapersimages.com/wp-content/uploads/2014/01/Winter-Tiger-Wild-Cat-Images.jpg','A fearsome tiger, lounging in the snow')
```
They should return, respectively:
```python
"<img src='http://www.hdwallpapersimages.com/wp-content/uploads/2014/01/Winter-Tiger-Wild-Cat-Images.jpg' />"
"<img src='http://www.hdwallpapersimages.com/wp-content/uploads/2014/01/Winter-Tiger-Wild-Cat-Images.jpg' alt='A fearsome tiger, lounging in the snow' />"
```
If there is no alt parameter passed in, no alt attribute should be set on the image.

## Divs
Divs are the swiss army knives of frontend developers. Useful for grouping elements and applying any kind of style, they are particularly nice when you start using complex CSS selectors.

Divs aren't all that useful on their own though. They need classes and ids so that we can target them with CSS. Your create_div function should accept an argument for the content within the div as well as optional arguments for intended class and id.

Potential Calls:
```python
create_div("<h1>Seussical</h1><p>What would happen if we let musicians reinterpret Dr. Seuss's work?</p>")
create_div("I'm not sure, but it'll be silly!", div_class="silly")
create_div("<img src='images/sillypic.jpg' />", div_id="sillypic")
```
And responses:
```python
"<div><h1>Seussical</h1><p>What would happen if we let musicians reinterpret Dr. Seuss's work?</p></div>"
"<div class='silly'>I'm not sure, but it'll be silly!</div>"
"<div id='sillypic'><img src='images/sillypic.jpg' /></div>"
```

## Head and Body
The head and body are pretty easy - just tags wrapped around contents.

Lots of your functions seem to do very similar things... Maybe you could consolidate your code with a helper function!

Call:
```python
create_head("Here's the head!")
create_body("Here's the body!")
```
Response:
```python
"<head>Here's the head!</head>"
"<body>Here's the body!</body>"
```

## Page
A valid HTML page has a doctype declaration and wraps everything else in an `<html>` tag. Write a function that takes the contents of a page as the argument, and returns a valid HTML page, like this:

This:
```python
create_page("Just pretend this is a head and body, full of great things")
```
Returns:
```python
"<!DOCTYPE html><html>Just pretend this is a head and body, full of great things</html>"
```

## Element
It's a pain to write functions for every single HTML element - there are some 100 more that we haven't gotten to! Instead of writing that many functions, create a function that takes the type of element as an argument, so that the user can create whatever kind of element they want. It should be able to have content inside and have attributes passed in as a dictionary.

Some sample calls, with the responses inline:
```python
create_element("section","I hear a Who!",{'class':'Horton'})
>>>"<section class='Horton'>I hear a Who!</section>"
create_element("em","I do not like them, Sam I Am!",{'id'='phrase'})
>>>"<em id='phrase'>I do not like them, Sam I Am!</em>"
create_element("form",create_element("button","Submit",{'type':'submit'}),{'action':'/postdata', 'method':'POST'})
>>>"<form action='/postdata' method='POST'><button type='submit'>Submit</button></form>"
```
That last one was tricky - it called the create_element function *from inside the create_element function*! Since the function returns a string, the inner call executes first, and the value it returns gets passed in as the argument to the outer call.

The create_element function is really general - if you haven't already, you can use it to rewrite your other functions. Code reuse is better than redundancy!

Make that final test pass! You got this!

## Bonus Challenges
That was lots of code to write. Congratulations! If you enjoyed it and want more, here are even more things to do:
- What kinds of elements aren't possible to generate with your functions? Write new functions to address the gaps!
- Write an interface for your functions, so that someone without technical skills could use them.
- The HTML that gets generated is pretty hard to read, however valid it may be. Make a function that formats html to be more readable.
- Think about what kinds of input might result in your functions generating broken HTML. What kinds of characters would make your generator break? Read up on HTML escaping to find out how to protect your users and your system from these kinds of vulnerabilities!
- Write CSS generating functions.
- Think about how an HTML parser would work - like the generator, but in reverse! Check out the source code for Beautiful Soup.
