
Technology used:
django framework
elephant postgresql database
python
css3
html5
js
bootstrap
jquery
google api

# **The Deepest Cleaning** 

I built this website to the people who would like to clean their house or for airbnb house's hosts who are looking for a new cleaning company. The deepest cleaning website has it is own booking system what the user can use after registration and they can leave a review as well with pictures if they would like to. They can edit the bookings until it is pending (change time slots or date), but if it is already been approved the user can just cancel it. The review can be updated too. The website has all the information about the company and about the two types of cleaning which is general and deep cleaning, on the contact us page they can see on the map where the company is located. 

[You can try it here on the live website!](https://the-deepest-cleaning-vm.herokuapp.com/)

![Home page](./static/images/homepage.png)

## _**Contents**_

* [Features](#features)
    * [Future ideas](#future-ideas)

* [Design](#design)
    * [Colors](#colors)
    * [Font](#font)
    * [Images](#images)
    * [Audio](#audio)

* [Testing](#testing)
    * [W3C Validator](#w3c-validator)
    * [CSS Validator](#css-validator)
    * [Lighthouse](#lighthouse)
    * [Manual testing](#manual-testing)
    * [Solved bugs](#solved-bugs)
    * [Known bugs](#known-bugs)

* [Deployment](#deployment)

* [Credits](#credits)
    

## _**Features**_

I created a website where the user can book an appoitment to two type of cleaning services and if would like even can leave a review with or without a picture. The user has to log in/ register first to see or use all the features.

![Booking](./static/images/booking.png)
![Review](./static/images/reviews.png)

 The user can check if the booked appoitment either is still pending or has been approved.
![Approve/Pending](./static/images/pending-approve-bookings.png)

And if the user wish can change the still pending booking but which has been approved can not been edited just delete it.
![Edit](./static/images/edit-booking.png)
![Delete](./static/images/delete-booking.png)

I hope everybody found this website useful and easy to navigate on even if the cleaners will not turn up for the booked dates. As always there is so many things what I would like to do to improve my website with further features.

 
 ### _Future ideas:_
  * I would like to send e-mails when the user registered/booked an appoitment 
  * I would like to send an e-mail to confirm the booking.
  * Make a contact form where the user can ask anything from the cleaning staff

  ## _**Design**_

  * ### _Colors:_
    * I choose a dark red color ( rgba(112, 13, 0, 0.9) ) with 90% of opacity to header and footer which I think it is a good eye catching colour with a light grey (#D7DDE0) writing on it so it is easy to read and looks quite good.
    * The box which contains the forms and the booking/review informations is the same light grey what I used for the fonts earlier so it is fit in the website design and I have a basic black writing on it.
    * The buttons have been style as the action for example the pending/edit sections are marked as yellow, the delete button is red and the approved button is green as success.

  * ### _Font:_
    * I used a Google Font called Lato with regular (400) weight and add Italic style to all of the headers and normal for rest of the page.
 
  * ### _Images:_
    * I used an image about a very nice clean, tidy kitchen so the users can see straight this company is trying to do the best service what they can.


## _**Testing**_

* ### _W3C Validator:_
    * I got back the following message : Document checking completed. No errors or warnings to show. from the official [W3C Website](https://validator.w3.org/nu/?doc=https%3A%2F%2Fthe-deepest-cleaning-vm.herokuapp.com%2F)

* ### _CSS Validator:_
    * I got back the following message: Sorry! We found the following errors (16)
    URI : https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css from the [Jigsaw Validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fthe-deepest-cleaning-vm.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en) which is bootstrap fault my own CSS has no Error!

* ### _Lighthouse:_
    * I done the lighthouse check through an incognito because that is when I got back the true result which were the following:

    ![Image about the lighthouse results](./static/images/lighthouse.png)

    The performance keep jumping up and down but always still in the green area the best practices is a bit lower because I used jQuery and the Google Maps API.

* ### _Manual testing:_
    * 

![mobile welcome page](./assets/images/readme-images/mobile-welcome.jpg) ![mobile categories](./assets/images/readme-images/mobile-cat.jpg)

s ![iPad welcome](./assets/images/readme-images/ipad-welcome.jpg) ![iPad questions](./assets/images/readme-images/ipad-questions.jpg)

 * ### _Solved bugs_:

    1. when i wrote a review it has not been sent to the database
    I did the "makemigrations" command loads of times but did not actually "migrate" it. that is why the database was not connected properly

    2. I made the form to leave a review but it did not show up on the template
    I was using a class based formview to render the template but I have not get the context data so the form did not show up

    3. I had a problem with the edit review/booking I could not pull the data which was already been wrote in the review or been booked in a modal
    I had a nice session with the tutors about it and at the end Ger said the big issues was I had to make a separate html for the edit where I can bring up the review/booking with the right id.

    4. When the user had to write the date for cleaning date there was no calendar just had to put in manually.
    Lucky for me the mentor showed me a solution with a widget in the forms and all was good.

    5. I couldn not show the validation message when the user choose a day in the past.
    The issue was I redirected the site to the home page after form has been done and the user could not see any message but the easy solution wwas just render it.

    6. approve button not working
    change the integerfield to boolean field and toggle instead of a form

    7. after deployment to heroku the static files are not found
    it happaned because the Debug in the settings was on True and I deployed like that, after I changed it to False everything went perfect.

 * ### _Known bugs:_

    1. I just found one bug what I know which is shows in the JSHint report. The categories is an unused variable, which is really not but the categories function using an 'onclick' method instead of the event listener and the JSHint can not read other files that is why I have this trouble. I will make sure it is change to the event listener in the future.

## _**Deployment**_

This site was deployed to GitHub Pages by following these steps:
1. Login or Sign Up to [GitHub](www.github.com).
2. Create a new repository named "spiderman-quiz".
3. Once created, click on "Settings" on the navigation bar under the repository title.
4. Scroll down to "GitHub Pages".
5. Under "Source", choose which branch to deploy. I chose "master", but this is sometimes shown as "main".
6. Choose which folder to deploy from, usually "/root".
7. Click "Save", then wait for it to be deployed. It can take some time for the page to be fully deployed.
8. Your URL will be displayed above "Source".
9. [Live website](https://viktormathe.github.io/spiderman-quiz/)



* ## _**Credits**_

    *  I download a Spider-Man themed font from the [1001 Fonts website](https://www.1001fonts.com/homoarakhn-font.html), which is free to use for everybody and applyed it on the welcome page and the copyright information on the footer.

    * The rest of the page is using a Comic Neue font from the [Google Fonts](https://fonts.google.com/specimen/Comic+Neue?preview.text=Questions&preview.text_type=custom&query=comic).

    * Source to the images: 
                  [Welcome image](https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/942d6891-f116-4a84-9c4e-cd6f2e736369/dcpnqvz-2d29d21a-4cbf-4e9e-8214-24183b45cd15.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzk0MmQ2ODkxLWYxMTYtNGE4NC05YzRlLWNkNmYyZTczNjM2OVwvZGNwbnF2ei0yZDI5ZDIxYS00Y2JmLTRlOWUtODIxNC0yNDE4M2I0NWNkMTUucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.uBlCPfGnjbFg5LKbg3auyL3NnGNc01obaH6XPJLddGI) , 
                  [Mobile welcome image](https://unsplash.com/photos/PXjQaGxi4JA) , [Main background](https://my4kwallpapers.com/wp-content/uploads/2020/09/Spiderman-4k-Wallpaper.jpg) , [Mobile background](https://1.bp.blogspot.com/-Bj2PS8yDKfM/YCn0zy8-AFI/AAAAAAAADOI/r7yy_WLMlh0XSvmV84dxj2FxRLYSUIUJQCLcBGAsYHQ/s600-rw/spiderman-back-logo-peter-parker-heroscreen.cc-hd-mobile-8.1933.jpg) , [Low score](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTk7K4DgqTRZRqY7biRhJQJkUqpkKu4ygquHw&usqp=CAU) , [Mid score](https://cdn.vox-cdn.com/thumbor/SLhFTTOcnZnb-PPIiJumu0WDY4Y=/85x0:1014x619/1200x800/filters:focal(85x0:1014x619)/cdn.vox-cdn.com/uploads/chorus_image/image/45660688/spiderman-marvel.0.0.jpg) , [High score](https://images.thedirect.com/media/article_big/Spider-man-logos.jpg?imgeng=cmpr_75/)

    * I found the theme song on the [YouTube](https://www.youtube.com/watch?v=j8deCNfNjO4&list=LL&index=2) which has no copyright on it and I could download it from the following [link](https://drive.google.com/file/d/1nwQRvlF6HnAgeZIeMmzKsoG1iGTKsz80/view).