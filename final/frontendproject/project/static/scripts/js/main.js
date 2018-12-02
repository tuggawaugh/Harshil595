(function(){function r(e,n,t){function o(i,f){if(!n[i]){if(!e[i]){var c="function"==typeof require&&require;if(!f&&c)return c(i,!0);if(u)return u(i,!0);var a=new Error("Cannot find module '"+i+"'");throw a.code="MODULE_NOT_FOUND",a}var p=n[i]={exports:{}};e[i][0].call(p.exports,function(r){var n=e[i][1][r];return o(n||r)},p,p.exports,r,e,n,t)}return n[i].exports}for(var u="function"==typeof require&&require,i=0;i<t.length;i++)o(t[i]);return o}return r})()({1:[function(require,module,exports){
var DynamicSearch = React.createClass({displayName: "DynamicSearch",

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

  onKeyDown: function(event){
        // 'keypress' event misbehaves on mobile so we track 'Enter' key via 'keydown' event
        if (event.key === 'Enter') {
			console.log("Enter Key!");
			console.log(event.target.value);
			event.preventDefault();
			event.stopPropagation();
			window.open('midterms/', "_blank")
			window.open('midterms/bpatel/?name='+event.target.value, "_blank")
			window.open('midterms/grubin/?name='+event.target.value, "_blank")
			window.open('midterms/hshah/?name='+event.target.value, "_blank")
			window.open('midterms/rwilliams/?name='+event.target.value, "_blank")
		  
		  
//          this.onSubmit();
        }
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
      React.createElement("div", null, 
        React.createElement("input", {type: "text", value: this.state.searchString, onChange: this.handleChange, onKeyDown: this.onKeyDown, placeholder: "Enter Ticker"}), 
        React.createElement("ul", null, 
           countries.map(function(country){ return React.createElement("li", null, country.name, " ") }) 
        )
      )
    )
  }

});

//var countries2 = stockSymbols;

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


ReactDOM.render(
  React.createElement(DynamicSearch, {items:  countries }),
  document.getElementById('main')
);

},{}]},{},[1]);
