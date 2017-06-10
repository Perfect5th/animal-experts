var React = require('react');
var ReactDOM = require('react-dom');

class Search extends React.Component {
  render() {
    return (
      <div>
        <div className="prompt search-prompt">
          <div className="prompt-text search-prompt-text">
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
        <div className="results-box"></div>
        <div className="prompt select-prompt">
          <div className="prompt-text search-prompt-text">
            <p>
              Show me experts in the field of
            </p>
          </div>
          <div className="search-box">
            <div className="search-wrap">
              <div className="search-padding">
                <select className="expert-search">
                  <option value="0"></option>
                  <option value="1">Value 1</option>
                  <option value="2">Value 2</option>
                  <option value="3">Value 3</option>
                </select>
              </div>
            </div>
          </div>
        </div>
        <div className="results-box"></div>
      </div>
    )
  }
};

ReactDOM.render(<Search />, document.getElementById('app'));
