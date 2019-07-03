<template>
  <div class="page">
  <div class="page">
      <div class="config-container">
        <div class="config-box">
            <div class="config-item">
              <el-upload
                class="upload-demo"
                drag
                :action="uploadURL"
                multiple show-file-list
                :auto-upload="false"
                :accept="acceptFileTypes"
                ref="upload"
                >
                <i class="el-icon-upload"></i>
                <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
                <div class="el-upload__tip" slot="tip">只能上传excel文件</div>
              </el-upload>
            </div>
            <div class="config-item">
                <el-button class="btnbgcolor" @click="handleUpload">提交</el-button>
            </div>
        </div>
    </div>
  </div>
</div>
</template>

<script>
import Api from '@/Api/excel-operation'
export default {
  data () {
    return {
      excelFiles: [],
      uploadURL: '',
      acceptFileTypes: ['application/vnd.ms-excel', 'application/vnd.ms-excel', 'application/vnd.ms-excel', 'application/vnd.ms-excel', 'application/vnd.ms-excel', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'].toString()
    }
  },
  created () {
    this.uploadURL = '/api/excel'
  },
  methods: {
    handleUpload () {
      let fileList = this.$refs.upload.$refs['upload-inner'].fileList
      let formData = new FormData()
      fileList.forEach(item => {
        formData.append('excel', item.raw)
      })
      Api.postExcel(formData).then(response => {
        this.$message.success('文件内容插入成功')
      }).catch(error => {
        this.$message.error(error.msg || '文件上传失败')
      })
    }
  }
}
</script>

<style lang="scss" scope>
@import '../assets/style.scss';
.page{
  width: 100%;
  height: 100%;
  margin: 10px auto;
  .head{
    width: 90%;
    margin-left: 2%;
  }
  .page{
    width: 30%;
    .config-container{
      margin: 50px auto;
    .config-box{
        display: flex;
        flex-direction: column;
        .config-item{
            margin:15px 0;
        }
    }
  }
  }
}
</style>
