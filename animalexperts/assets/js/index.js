var React = require('react');
var ReactDOM = require('react-dom');

var Search = React.createClass ({
  render: function() {
    return (
      <div>
        <div className="search-prompt-text">
          <p>
            Find me someone who is an expert in
          </p>
        </div>
        <div className="search-box">
          <div className="search-wrap">
            <div className="search-padding">
              <input type="text" className="expert-search" />
            </div>
          </div>
        </div>
      </div>
    )
  }
});

ReactDOM.render(<Search />, document.getElementById('app'));
