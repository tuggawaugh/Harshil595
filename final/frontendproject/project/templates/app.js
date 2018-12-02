import React from 'react'
import DOM from 'react-dom'
import Autocomplete from '../../lib/index'
import { getStates, fakeRequest } from '../../lib/utils'
import stockSymbols from '../../csvjson2.json';


class App extends React.Component {

  state = {
    value: '',
    unitedStates: getStates(),
  }

  requestTimer = null

  render() {
    return (
      <div>
        <h1>Stock Look-up</h1>
        <p>
          This is a simple front-end that provides suggestions based on the typed search input. Suggested securities are listings from common US exchanges (NYSE, NASDAQ, AMEX).
        </p>
        <label htmlFor="states-autocomplete">Enter a ticker:</label>
        <Autocomplete
          inputProps={{ id: 'states-autocomplete' }}
          wrapperStyle={{ position: 'relative', display: 'inline-block' }}
          value={this.state.value}
          items={this.state.unitedStates}
          getItemValue={(item) => item.name}
          onSelect={(value, item) => {
            // set the menu to only the selected item
            this.setState({ value, unitedStates: [ item ] })
            // or you could reset it to a default list again
            // this.setState({ unitedStates: getStates() })
          }}
          onChange={(event, value) => {
			console.log("on change event!");
            this.setState({ value })
            clearTimeout(this.requestTimer)
            this.requestTimer = fakeRequest(value, (items) => {
              this.setState({ unitedStates: items })
            })
          }}
          renderMenu={children => (
            <div className="menu">
              {children}
            </div>
          )}
          renderItem={(item, isHighlighted) => (
            <div
              className={`item ${isHighlighted ? 'item-highlighted' : ''}`}
              key={item.abbr + item.name + item.exchange}
            >{''+ item.abbr + '  ' + item.name + '  ' + item.exchange}</div>
          )}
        />
      </div>
    )
  }
}

DOM.render(<App/>, document.getElementById('container'))

if (module.hot) { module.hot.accept() }