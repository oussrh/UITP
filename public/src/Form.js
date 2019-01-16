import React, { Component } from 'react';
import axios from 'axios';


import Incident from './Incident';


class Form extends Component {
  constructor(c,incids){
  super()
  c=1;
  incids = []
  while(c < 30){
    incids.push({id:c,frequence:0,commentaire:"",motivation:"",idRapport:1,idTransport:2});
    c++;
  }
    this.state = {
      entries : incids
    } 
}
  handelInput = (e) =>{
    const incidId= (e.target.parentElement.id)-1;
    const inputName = e.target.name;
    const inputValue = e.target.value;
    // eslint-disable-next-line
      this.setState()
      let entries = Object.assign({}, this.state);
      entries.entries[incidId].inputName = inputValue;
      this.setState(entries);

      console.log(this.state.entries)
  }

  onSubmit = (e) => {
    e.preventDefault();
    axios
      .post('http://127.0.0.1:8000/api/detail/', this.state.entries)
            .then(function(response) {
                console.log(response);}) 
         .catch(function (error) {
                console.log(error);
            });
           }
  render() {
    return (
      <form>
        <Incident inputHandel={this.handelInput}/>
        <input type="submit" value="Submit" onClick={this.onSubmit} />
      </form>
    );
  }
}

export default Form;