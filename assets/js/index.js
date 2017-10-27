var React = require('react');
var ReactDOM = require('react-dom');

class Search extends React.Component {

  constructor(props) {
    super(props);
    this.handleSearchBoxChange = this.handleSearchBoxChange.bind(this);
    this.handleSelectBoxChange = this.handleSelectBoxChange.bind(this);
    this.state = { data: null };
  }

  loadSearchResults(searchParam) {
    // TODO: make this occur onChange of search box
    var r = new XMLHttpRequest();
    r.open("GET", "/api/experts?q=" + encodeURIComponent(searchParam), true);
    r.onreadystatechange = () => {
      if (r.readyState != 4 || r.status != 200) return;
      this.setState({ data: JSON.parse(r.responseText) });
    };
    r.send();
  }

  handleSearchBoxChange(value) {
    this.loadSearchResults(value);
  }

  handleSelectBoxChange(value) {
    return;
  }

  render() {
    const searchValue = this.state.searchValue;

    return (
      <div>
        <div className="prompt search-prompt">
          <div className="prompt-text search-prompt-text">
            <p>
              Find me someone who is an expert in
            </p>
          </div>
          <SearchBox
            value={searchValue}
            onSearchChange={this.handleSearchBoxChange} />
        </div>
        <SearchResults searchResults={this.state.data} />
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

  constructor(props) {
    super(props);
    this.state = { value: '' };

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.props.onSearchChange(event.target.value);
  }

  handleSubmit(event) {
    alert('A value was submitted: ' + this.props.value);
    event.preventDefault();
  }

  render() {
    return (
      <form onSubmit={this.handleSubmit}>
        <div className="search-box">
          <div className="search-wrap">
            <div className="search-padding">
              <input type="text" className="expert-search" value={this.props.value} onChange={this.handleChange} />
            </div>
          </div>
        </div>
      </form>
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

  constructor(props) {
    super(props);
  }

  render() {
    if (this.props.searchResults) {
      var expertNodes = this.props.searchResults.results.map(expert => {

        var fieldItems = expert.fields.map(field => {
          return <li key={field.url}><a href={field.url}>{field.name}</a></li>;
        });

        return (
          <div className="result-item" key={expert.url}>
            <div className="expert-left-block">
              <h3>{expert.title} {expert.first_name} {expert.last_name}</h3>
              <p className="expert-affiliation">{expert.affiliation}</p>
            </div>
            <div className="expert-subjects">
              {expert.subjects}
            </div>
            <div className="expert-fields">
              <ul>{fieldItems}</ul>
            </div>
            <div className="expert-website">
              <a href={expert.website}>{expert.website}</a>
            </div>
            <div className="expert-description">
              {expert.description}
            </div>
          </div>
        );
      })
    }

    return (
      <div className="results-box">
        <div className="results-list">
          {expertNodes}
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
