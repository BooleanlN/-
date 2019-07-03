<template>
<el-main class="main-bar">
                <div class="main-header">
                   <el-breadcrumb separator="/">
                    <el-breadcrumb-item :to="{ path: '/' }">知识库手动输入</el-breadcrumb-item>
                    </el-breadcrumb>
                </div>
                <div class="main-content">
                    <el-table :data="tableData" style="width:100%">
                        <el-table-column type="index" width="75px" label="序号">
                        </el-table-column>
                        <el-table-column  label="故障现象"
                        prop="faultapperence">
                          <template  slot-scope="scope">
                              <el-input v-model="tableData[scope.$index].faultapperence" placeholder=""></el-input>
                          </template>
                        </el-table-column>
                        <el-table-column  label="故障原因"
                        prop="faultreason">
                        <template  slot-scope="scope">
                              <el-input v-model="tableData[scope.$index].faultreason" placeholder=""></el-input>
                          </template>
                        </el-table-column>
                        <el-table-column  label="故障处理"
                        prop="faulthandle">
                        <template  slot-scope="scope">
                              <el-input v-model="tableData[scope.$index].faulthandle" placeholder=""></el-input>
                          </template>
                        </el-table-column>
                        <el-table-column label="操作" width="200px">
                            <template slot-scope="scope">
                                <el-button size="mini" @click="handleDelete(scope.row,scope.$index)" type="danger">删除</el-button>
                            </template>
                        </el-table-column>
                    </el-table>
                  <div style="margin:10px auto;width:100%;text-align:center;">
                      <el-button type="primry" class="btnbgcolor" @click="addnewline">新增一行</el-button>
                      <el-button type="primry" class="btnbgcolor" @click="handleAdd">提交</el-button>
                  </div>
                </div>
</el-main>
</template>

<script>
import importApi from '@/Api/knowledge-operation'
export default {
  data () {
    return {
      tableTitles: [
        {
          label: '故障现象',
          prop: 'faultapperence'
        }, {
          label: '故障原因',
          prop: 'faultreason'
        }, {
          label: '故障处理',
          prop: 'faulthandle'
        }
      ],
      tableData: [
        {
          faultapperence: '',
          faultreason: '',
          faulthandle: ''
        }
      ]
    }
  },
  methods: {
    handleEdit (row, index) {},
    handleDelete (row, index) {
      this.tableData.splice(index, 1)
    },
    addnewline () {
      this.tableData.push({
        faultapperence: '',
        faultreason: '',
        faulthandle: ''
      })
    },
    handleAdd () {
      let formData = new FormData()
      let apperence = []
      let reason = []
      let handle = []
      this.tableData.forEach(item => {
        apperence.push(item.faultapperence)
        reason.push(item.faultreason)
        handle.push(item.faulthandle)
      })
      formData.append('faultApperence', apperence)
      formData.append('faultReason', reason)
      formData.append('faultHandle', handle)
      importApi.insertKnowledgeDatas(formData).then(response => {
        console.log(response)
        this.$message.success('数据插入成功')
        this.tableData = [
          {
            faultapperence: '',
            faultreason: '',
            faulthandle: ''
          }
        ]
      }).catch(error => {
        this.$message.error(error.msg || '数据插入失败')
      })
    }
  }
}
</script>

<style lang="scss" scope>
@import "../assets/style.scss"
</style>
