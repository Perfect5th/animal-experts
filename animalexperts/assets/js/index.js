var React = require('react');
var ReactDOM = require('react-dom');

var Search = React.createClass ({
  render: function() {
    return (
      <div>
        <h1>
          Find me someone who is an expert in
        </h1>
        <input type="text" />
      </div>
    )
  }
});

ReactDOM.render(<Search />, document.getElementById('app'));
