var DynamicSearch = React.createClass({

  // sets initial state
  getInitialState: function(){
    return { searchString: '' };
  },

  // sets state, triggers render method
  handleChange: function(event){
    // grab value form input box
    this.setState({searchString:event.target.value});
    console.log("scope updated!");
  },

  render: function() {

    var countries = this.props.items;
    var searchString = this.state.searchString.trim().toLowerCase();

    // filter countries list by value from input box
    if(searchString.length > 0){
      countries = countries.filter(function(country){
        return country.name.toLowerCase().match( searchString );
      });
    }

    return (
      <div>
        <input type="text" value={this.state.searchString} onChange={this.handleChange} placeholder="Enter Ticker" />
        <ul>
          { stockSymbols.map(function(stockSymbols){ return <li>{stockSymbols.name} </li> }) }
        </ul>
      </div>
    )
  }

});

// list of countries, defined with JavaScript object literals
var countries = [
    {"name": "GE"},
    {"name": "F"},
    {"name": "BAC"},
    {"name": "SNAP"},
    {"name": "T"},
    {"name": "TWTR"},
    {"name": "NOK "},
    {"name": "ABEV"},
    {"name": "WFT"}
];

// import stockSymbols from '/Users/gordon.rubin/Documents/stevens/fe-595-ws/midterm/Harshil595/csvjson2.json';

ReactDOM.render(
  <DynamicSearch items={ countries } />,
  document.getElementById('main')
);