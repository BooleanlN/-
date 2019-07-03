<template>
<el-main class="main-bar">
                <div class="main-header">
                   <el-breadcrumb separator="/">
                    <el-breadcrumb-item :to="{ path: '/' }">知识库列表</el-breadcrumb-item>
                    </el-breadcrumb>
                </div>
                <div class="main-action">
                   <span class="main-action-span"><i class="el-icon-info"></i>故障现象总数：{{faultCount}}</span>
                   <span class="main-action-span"><i class="el-icon-info"></i>故障原因总数：{{faultReasonCount}}</span>
                   <span class="main-action-span"><i class="el-icon-info"></i>故障处理总数：{{faultHandleCount}}</span>
                </div>
                <div class="main-content">
                    <el-table :data="tableData" style="width:100%">
                        <el-table-column type="index" width="75px" label="序号">
                        </el-table-column>
                        <el-table-column v-for="(title,index) in tableTitles" :key="index" :label="title.label"
                        :property="title.prop"
                        >
                        </el-table-column>
                        <el-table-column label="操作" width="200px">
                            <template slot-scope="scope">
                                <!-- <el-button size="mini" @click="handleEdit(scope.row,scope.$index)">
                                    编辑
                                </el-button> -->
                                <el-button size="mini" @click="handleDelete(scope.row,scope.$index)" type="danger">删除</el-button>
                            </template>
                        </el-table-column>
                    </el-table>
                    <div class="pagination">
                         <el-pagination
                            :page-size="8"
                            background
                            layout="prev, pager, next"
                            :current-page.sync="pageno"
                            :total="total"
                            @current-change="handlePage"
                            >
                         </el-pagination>
                    </div>
                </div>
</el-main>
</template>

<script>
/* eslint-disable */
import Api from '@/Api/knowledge-operation'
export default {
  data () {
    return {
      tableTitles: [
        {
          label: '故障现象',
          prop: 'faultApperence'
        }, {
          label: '故障原因',
          prop: 'faultReason'
        }, {
          label: '故障处理',
          prop: 'faultHandle'
        }
      ],
      faultReasonCount: 0,
      faultHandleCount: 0,
      faultCount: 0,
      tableData: [],
      pagecount: 0,
      total: 0,
      pageno: 1,
      pagesize: 8
    }
  },
  created () {
    this.getFaultList()
  },
  methods: {
    getFaultList () {
      let formData = new FormData()
      formData.append('pageno',this.pageno)
      formData.append('pagesize',this.pagesize)
      Api.getKnowledgeTable(formData).then(response => {
        this.tableData = response.data.data
        this.faultCount = response.data.fault_apperence_count
        this.faultReasonCount =  response.data.fault_reason_count
        this.faultHandleCount = response.data.fault_handle_count
        this.pageno = response.data.pageno
        this.total = response.data.fault_apperence_count
      }).catch(error => {
        this.$message.success('获取知识库失败')
      })
    },
    // 页码
    handlePage () {
      this.getFaultList()
    },
    // 删除
    handleDelete (row, index) {
      const h = this.$createElement
      this.$msgbox({
        title:'删除提示',
        message: h('p',null,[
          h('span',null,'确定删除该条知识库记录?')
        ]),
        showCancelButton:true,
        confirmButtonText:'确定',
        cancelButtonText:'取消',
        callback: action => {
          if(action === 'confirm'){
            let form = new FormData()
            form.append('faultid',row.faultid)
            Api.deleteKnowledgeData(form).then(response => {
              this.$message.success('删除成功')
              this.tableData.splice(index,1)
              this.getFaultList()
            }).catch(error => {
              this.$message.error('删除失败')
            })
          }
        }
      })
    }
  }
}
</script>

<style lang="scss" scope>
@import "../assets/style.scss"
</style>
