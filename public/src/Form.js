import React, { Component } from 'react';

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
    const incidId= e.target.parentElement.id;
    const inputName = e.target.name;
    const inputValue = e.target.value;
    // eslint-disable-next-line
      this.setState()
      let entries = Object.assign({}, this.state);
      entries.entries[incidId].inputName = inputValue;
      this.setState(entries);

      console.log(this.state.entries)
  }
  render() {
    return (
      <form>
        <Incident inputHandel={this.handelInput}/>
        <input type="submit" value="Submit" />
      </form>
    );
  }
}

export default Form;