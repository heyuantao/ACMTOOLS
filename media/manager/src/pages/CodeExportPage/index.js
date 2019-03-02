import React from "react";
import CodeExportContestList from "./CodeExportContestList";

class CodeExportPage extends React.Component{
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
                <CodeExportContestList></CodeExportContestList>
            </div>
        )
    }
}

export default CodeExportPage