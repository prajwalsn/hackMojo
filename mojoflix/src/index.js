import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';

function Get(yourUrl){
    var Httpreq = new XMLHttpRequest();
    Httpreq.open("GET",yourUrl,false);
    Httpreq.send(null);
    return Httpreq.responseText;          
}

const MovieCard = ( props ) => 
    (
        <div className="card">
            <img src= { props.moviePosterURL } className="card-img-top" alt="..."  ></img>
            <div className="card-body"> 
                <h5 className="card-title"> { props.movieTitle } </h5>
                <h6 className="card-subtitle mb-2 text-muted"> { props.movieDirector } </h6>
                <p className="card-text"> { props.movieDescription } </p>
                <button type="button" className="btn btn-primary" onClick = {props.func}> Watch </button>
            </div>
        </div>
    );

class Container extends React.Component
{
    constructor(props)
    {
        super(props);
        this.state = {
            videoPacks : [],
            videos : [],
        }

        this.addMovie("Inception");
        this.addMovie("Split");
        this.addMovie("Primer");
        this.addMovie("Titanic");
        this.addMovie("Jaws");
        this.addMovie("The Dark Knight");


        this.state.videos.push("Psycho");
    }

    createFunction( func , name )
    {
        return () => { this.watchMovie(name) }
    }

    watchMovie( name )
    {
        this.state.videoPacks.splice( this.state.videoPacks.indexOf(name) , 1 );
        this.state.videos.push( name );
        this.forceUpdate();
        
    }

    getJSX( name )
    {
        var movie = JSON.parse(Get("http://www.omdbapi.com/?t=" + name + "&apikey=b4cb0091"));
        
        console.log(movie);
        
        let imoviePosterURL = movie.Poster;
        let imovieTitle = movie.Title;
        let imovieDirector = movie.Director;
        let imovieDescription = movie.Plot; 
        let newFunc = this.createFunction( this.lol , imovieTitle )

        let mv1 = < MovieCard func = { newFunc } moviePosterURL = { imoviePosterURL } movieTitle = { imovieTitle } movieDirector = {imovieDirector} movieDescription = { imovieDescription }/>
        return mv1;
    }

    addMovie( name )
    {
        this.state.videoPacks.push(name);
    }

    register()
    {
    }

    render() {

        return(
            <div>
                <h1> Videos </h1>
                <form className ="form-inline md-form mr-auto mb-4" id = "f">
                    <input id = 's' className="form-control mr-sm-2" type="text" placeholder="Movie Name" aria-label="Add"/>
                    <button className="btn aqua-gradient btn-rounded btn-sm my-0" form = "f" type="submit" onClick = { () => { this.state.videoPacks.push(document.getElementById('s').value); this.forceUpdate() } } >Search</button>
                </form>
                <div className = "card-columns">
                    {this.state.videoPacks.map( card => this.getJSX(card))}
                </div>
                <h1> Video Packs </h1>
                <div className = "card-columns">
                    {this.state.videos.map( card => this.getJSX(card))}
                </div>
            </div>

        );
    }
}

ReactDOM.render( <Container/> , document.getElementById('root'));
