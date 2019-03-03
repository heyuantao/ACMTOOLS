import React from "react";
import {hashHistory, Link} from "react-router";
import { Row, Col, Form, Button, Table, Icon} from 'antd';
import { fromJS } from "immutable";
import Settings from "../../Settings";

const FormItem = Form.Item;
const req = Settings.request;
const table_data_api_url = Settings.anti_cheating_contest_api_url;

class AntiCheatingContestList extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            fetching: false,
            pagination: fromJS({ total: 0, pageSize: 8, current: 1}),
            tableData: fromJS([]),
        }
    }
    componentWillReceiveProps(props) {
        //this.fetchTableListData()
    }
    fetchTableListData() {
        const url = table_data_api_url;
        const params = this.state.pagination.toJS();
        this.setState({fetching:true})
        req.get(url, {params:params}).then(function (response) {
            let tableData = fromJS(response.data.items);
            let paginationData = fromJS(response.data.pagination);
            this.setState({pagination:paginationData});
            this.setState({ tableData: tableData });
            this.setState({fetching:false});
        }.bind(this)).catch(function (error) {
            this.setState({fetching:false});
        }.bind(this))
    }
    handleReCalc(contest_id){
        const url = table_data_api_url+contest_id+"/";
        const params = {'status':'pending'};
        req.put(url, {params:params}).then(function (response) {
            this.fetchTableListData();
        }.bind(this)).catch(function (error) {

        }.bind(this))

    }
    componentDidMount() {
        this.fetchTableListData()
    }
    handleTableChange(pagination, filters, sorter){
        let newPagination=fromJS(pagination)
        this.setState({pagination:newPagination},()=>{this.fetchTableListData()})
    }
    tableColumnFormat() {
        let tableColumn = [
            { title: "考试编号", dataIndex: "contest_id", key: "contest_id" },
            { title: "考试名称", dataIndex: "title", key: "title" },
            { title: "更新时间", key: "in_date",
                render: (text, record) => (
                    <div>
                        {(record.status!=='none')&&<span>{record.in_date}</span>}
                        {(record.status==='none')&&<span>未就绪</span>}
                    </div>
                )
            },
            {
                title: "数据处理状态",  key: "status" ,
                render: (text, record) => (
                    <div>
                        {(record.status==='none')&&<Icon type="question-circle" theme="twoTone" twoToneColor="#eb2f96" />}
                        {(record.status==='pending')&&<Icon type="sync" spin/>}
                        {(record.status==='finished')&&<Icon type="check-circle" theme="twoTone" twoToneColor="#52c41a"/>}
                        {(record.status==='error')&&<Icon type="question-circle" theme="twoTone" twoToneColor="#eb2f96" />}
                    </div>
                )
            },
            {
                title: "状态描述", key: "desc",
                render: (text, record) => (
                    <div>
                        {(record.status==='none')&&<a disabled={true}>未就绪</a>}
                        {(record.status==='pending')&&<a disabled={true}>正在处理</a>}
                        {(record.status==='finished')&&<Link to={"/anticheating/contestsubmit/"+record.id+"/analyze/"}>查看结果</Link >}
                        {(record.status==='error')&&<a>出现错误</a>}
                    </div>
                )
            },
            {
                title: "操作", key: "action",
                render: (text, record) => (
                    <div>
                        {(record.status==='none')&&<a onClick={()=>{this.handleReCalc(record.contest_id)}}>开始分析</a>}
                        {(record.status==='pending')&&<a disabled={true}>请等待</a>}
                        {(record.status==='finished')&&<a onClick={()=>{this.handleReCalc(record.contest_id)}}>重新分析</a >}
                        {(record.status==='error')&&<a onClick={()=>{this.handleReCalc(record.contest_id)}}>重新分析</a>}
                    </div>
                )
            }
        ];
        return tableColumn;
    }
    handleFetchTableData(){
        this.fetchTableListData()
    }
    render() {
        return (
            <div>
                <Row type="flex" justify="space-between" align="middle" >
                    <Col>
                        <h2>考试替考分析</h2>
                    </Col>
                    <Col>
                        <Button onClick={() => { this.handleFetchTableData() }} type="primary" >刷新</Button>
                    </Col>
                </Row>
                <Row type="flex" justify="space-between" align="middle">
                    <Col span={24}>
                        <div style={{ marginBottom: "15px" }}></div>
                        <Table dataSource={this.state.tableData.toJS()} rowKey="id" pagination={this.state.pagination.toJS()}
                            onChange={(pagination, filters, sorter)=>{this.handleTableChange(pagination, filters, sorter)}}
                            columns={this.tableColumnFormat()}
                            loading={this.state.fetching}
                        ></Table>
                    </Col>
                </Row>
            </div>
        )
    }
}

export default AntiCheatingContestList