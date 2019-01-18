import React, { Component } from 'react';
import axios from 'axios';


import Incident from './Incident';


class Form extends Component {
  constructor(c,incids) {
    super()
    this.state = {
      entries: [],
      lengIncidents: 0
    }
  }

  getLngIncidents = l => {
    this.count = 1;
    this.incids = []
    while (this.count < l) {
      this.incids.push({
        id: this.c,
        frequence: 0,
        commentaire: "",
        motivation: "",
        idRapport: 1,
        idTransport: 2
      });
      this.c++;
    }

    this.setState({entries:this.incids})
  }
  
  handelInput = (e) => {
    const incidId = (e.target.parentElement.id) - 1;
    // eslint-disable-next-line
    const inputName = e.target.name;
    const inputValue = e.target.value;
    // eslint-disable-next-line
    let entries = Object.assign({}, this.state);
    entries.entries[incidId][inputName] = inputValue;
    this.setState(entries);
  }

  onSubmit = (e) => {
    e.preventDefault();
    axios
      .post('http://127.0.0.1:8000/api/detail/', this.state.entries)
      .then(function (response) {
        console.log(response);
      })
      .catch(function (error) {
        console.log(error);
      });
  }
  render() {
    return (
      <form>
        <Incident inputHandel={this.handelInput} getLngIncidents={this.getLngIncidents}/>
        <input type="submit" value="Submit" onClick={this.onSubmit} />
      </form>
    );
  }
}

export default Form;