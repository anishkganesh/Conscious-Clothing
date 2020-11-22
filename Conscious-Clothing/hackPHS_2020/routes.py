from flask import render_template, flash
from hackPHS_2020 import app
from hackPHS_2020.forms import ClothingForm
from hackPHS_2020 import data_extraction, carbon_calculator

# note: shift + tab to indent one tab space backwards
# note: alt + j to select next occurrence of highlighted text


@app.route("/", methods=['GET', 'POST'])  # decorator
@app.route("/home", methods=['GET', 'POST'])
def home():
    form = ClothingForm()
    carbon_value = None;
    if form.validate_on_submit():
        url = form.link.data
        product_data = data_extraction.data_parser(url)
        carbon_value = carbon_calculator.give_value(product_data)
        if carbon_value < 9:
            flash("A Good Piece of Clothing to Add to Your Collection! " + "Carbon Unfriendliness: " + str(carbon_value)
                  + "%", 'success')
        elif carbon_value < 18:
            flash("A Reasonable Piece of Clothing to Add to Your Collection. " + "Carbon Unfriendliness: " + str(carbon_value) + "%",
                  'warning')
        else:
            flash("Not The Best of Clothing to Add to Your Collection! " + "Carbon Unfriendliness: " + str(carbon_value) + "%",
                  'danger')
        url1 = 'https://www.amazon.com/Emporio-Armani-Eagle-V-Neck-White/dp/B06VVKC94N/ref=sr_1_30?dchild=1&keywords=' \
               'armani+shirts&qid=1604838927&sr=8-30'
        url2 = 'https://www.amazon.com/Armani-Exchange-Mens-Crew-Black/dp/B0775SPV13/ref=sr_1_6?dchild=1&keywords=' \
               'armani+shirts&qid=1604838927&sr=8-6'
        url3 = 'https://www.amazon.com/Armani-Exchange-Solid-Colored-Basic/dp/B01MZ6AJ1J/ref=sr_1_15?dchild=1&' \
               'keywords=armani+t+shirts&qid=1604839040&sr=8-15'
        return render_template('home.html', form=form, url1=url1, url2=url2, url3=url3)
    return render_template('home.html', form=form)    # the variable posts can now be accessed from the html file
