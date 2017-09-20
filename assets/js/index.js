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
    // TODO: make this occur onChange of search box
    var r = new XMLHttpRequest();
    r.open("GET", "/api/experts", true);
    r.onreadystatechange = () => {
      if (r.readyState != 4 || r.status != 200) return;
      this.setState({ data: JSON.parse(r.responseText) });
    };
    r.send();
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
      var expertNodes = this.state.data.results.map(expert => {

        var fieldItems = expert.fields.map(field => {
          return <li key={field.url}><a href="{field.url}">{field.name}</a></li>;
        });

        return (
          <li key={expert.url}>
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
              {expert.website}
            </div>
            <div className="expert-description">
              {expert.description}
            </div>
          </li>
        );
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
