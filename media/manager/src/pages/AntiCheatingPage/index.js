import React from "react";
import AntiCheatingContestList from "./AntiCheatingContestList"

class AntiCheatingPage extends React.Component{
    constructor(props) {
        super(props);
        this.state = {
        }
    }
    componentDidMount() {
    }
    render() {
        return (
            <div style={{ padding: 24, background: "#fff"}}>
                <AntiCheatingContestList></AntiCheatingContestList>
            </div>
        )
    }
}

export default AntiCheatingPage