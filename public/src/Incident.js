import React, { Component } from 'react';
import axios from 'axios';

const url = "http://127.0.0.1:8000/api";
class Incident extends Component {
constructor(props) {
    super(props);
  this.state = {
    incidents:[],

  };
}
  componentDidMount(){
    axios.get(`${url}/incidents/`)
        .then( res => {
            
            this.setState({incidents: res.data});
        })
        .catch((err) => {
            console.log("AXIOS ERROR: ", err);
        })
  }
  render() {
    return (
      
      <div>
        <ul>
          {      
            this.state.incidents.map( x =>
              <div key={x.id} id={x.id} className="inputContainer">
              <label>{x.id}-{x.nomIncident}</label>
              <select name="frequence" onChange={this.props.handelInput}>
                <option value="0">0</option>
                <option value="1">1</option>
                <option value="2">2</option>
                <option value="3">3</option>
                <option value="4">4</option>
              </select>
              <input type="text" name="commentaire" onChange={this.props.inputHandel}/>
              <input type="text" name="motivation" onChange={this.props.inputHandel}/>
              </div>
            )
          }
        </ul>
      </div>
    );
  }
}

export default Incident;