import React from "react";
import {Layout} from "antd";

const { Footer } = Layout;

export default class PageFooter extends React.PureComponent {
    render() {
        return (
            <Footer style={{ textAlign:"center",padding: 10 }}>
                ZUA ©2018 郑州航空工业管理学院/计算机学院
            </Footer>
        )
    }
}