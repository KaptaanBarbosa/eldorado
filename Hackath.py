from flask import Flask
from flask import jsonify
import PosTagger

app = Flask(__name__)


@app.route('/')
def root():
    return 'Hello World!'

@app.route('/getTagText')
def gettagtext():
    ## to remove make the call post so that data comes from user side
    contentArray =['Starbucks is not doing very well lately.',
               'Overall, while it may seem there is already a Starbucks on every corner, Starbucks still has a lot of room to grow.',
               'They just began expansion into food products, which has been going quite well so far for them.',
               'I can attest that my own expenditure when going to Starbucks has increased, in lieu of these food products.',
               'Starbucks is also indeed expanding their number of stores as well.',
               'Starbucks still sees strong sales growth here in the united states, and intends to actually continue increasing this.',
               'Starbucks also has one of the more successful loyalty programs, which accounts for 30%  of all transactions being loyalty-program-based.',
               'As if news could not get any more positive for the company, Brazilian weather has become ideal for producing coffee beans.',
               'Brazil is the world\'s #1 coffee producer, the source of about 1/3rd of the entire world\'s supply!',
               'Given the dry weather, coffee farmers have amped up production, to take as much of an advantage as possible with the dry weather.',
               'Increase in supply... well you know the rules...']


    tagged=PosTagger.WordTagger.postag(contentArray)

    print("@@@@@",tagged);

    return jsonify(tagged);





if __name__ == '__main__':
    app.run(debug=True)