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
          <SearchBox />
        </div>
        <SearchResults />
        <div className="prompt select-prompt">
          <div className="prompt-text search-prompt-text">
            <p>
              Show me experts in the field of
            </p>
          </div>
          <SelectBox />
        </div>
        <SelectResults />
      </div>
    );
  }
};

class SearchBox extends React.Component {
  render() {
    return (
      <div className="search-box">
        <div className="search-wrap">
          <div className="search-padding">
            <input type="text" className="expert-search" />
          </div>
        </div>
      </div>
    );
  }
}

class SelectBox extends React.Component {
  render() {
    return (
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
    );
  }
}

class SearchResults extends React.Component {
  loadSearchResults() {
    $.ajax({
      url: '/api/experts/',
      datatype: 'json',
      cache: false,
      success: function(data) {
        this.setState({ data: data });
      }.bind(this)
    })
  }

  constructor(props) {
    super(props);
    this.state = { data: {} };
  }

  componentWillMount() {
    this.loadSearchResults();
  }

  render() {
    if (this.state.data.results) {
      var expertNodes = this.state.data.results.map(function (expert) {
        return <li key={expert.url}>{expert.title} {expert.first_name} {expert.last_name}</li>;
      })
    }

    return (
      <div className="results-box">
        <div className="results-list">
          <ul>
            {expertNodes}
          </ul>
        </div>
      </div>
    )
  }
};

class SelectResults extends React.Component {
  render() {
    return (
      <div className="results-box">
        <div className="results-list">
          <ul>
          </ul>
        </div>
      </div>
    )
  }
}

ReactDOM.render(<Search />, document.getElementById('app'));
