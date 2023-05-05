<template>
  <div>
    <div class="shangchuanbar" style="width: 100%; float: left">
      <ul :inline="true" class="demo-form-inline">
        <li>
          <el-upload
            class="upload-demo"
            :before-upload="beforeUpload"
            action=""
            :show-file-list="false"
            list-type="picture-card"
            :http-request="uploadFile"
            multiple
            :limit="10"
            :file-list="fileList"
            accept=".txt"
            :disabled="isSelected"
          >
            <i slot="default" class="el-icon-plus"></i>
          </el-upload>
        </li>
        <li>
          <div class="block">
            <el-select v-model="value" placeholder="请选择">
              <el-option
                v-for="item in options"
                :key="item.value"
                :label="item.label"
                :value="item.value"
              >
              </el-option>
            </el-select>
            <br />
          </div>
          <el-button @click="submit" class="shangchuan">点击上传</el-button>
          <div class="tishi">只能上传txt文件,且不超过4GB</div>
        </li>
      </ul>
    </div>
    <div style="float: left" class="file_list">
      <ul>
        <li>
          <h3>已上传通过文献</h3>
        </li>
        <li>
          <el-table
            :data="success_files"
            @row-click="handdle1"
            style="width: 100%"
            :row-style="{ height: '50px' }"
          >
            <el-table-column prop="title" label="文献名" width="150">
            </el-table-column>
            <el-table-column prop="field" label="文献领域" width="180">
            </el-table-column>
            <el-table-column prop="create_time" label="上传时间" width="100">
            </el-table-column>
          </el-table>
        </li>
      </ul>
      <el-pagination
        @size-change="handleSizeChange1"
        @current-change="handleCurrentChange1"
        :current-page="params1.currentpage"
        :page-size="params1.pageSize"
        layout="prev, pager, next"
        :total="total1"
        class="pagination1"
      >
      </el-pagination>
    </div>
    <div
      style="float: left"
      class="file_list"
      v-show="this.$store.getters.getIdentity"
    >
      <ul>
        <li>
          <h3>未审核的文献</h3>
        </li>
        <li>
          <el-table
            :data="wait_examine_files"
            style="width: 100%"
            @row-click="handdle2"
          >
            <el-table-column prop="title" label="文献名" width="150">
            </el-table-column>
            <el-table-column prop="field" label="文献领域" width="180">
            </el-table-column>
            <el-table-column prop="create_time" label="上传时间" width="100">
            </el-table-column>
          </el-table>
        </li>
      </ul>
      <el-pagination
        @size-change="handleSizeChange2"
        @current-change="handleCurrentChange2"
        :current-page="params1.currentpage"
        :page-size="params1.pageSize"
        layout="prev, pager, next"
        :total="total2"
        class="pagination2"
      >
      </el-pagination>
    </div>
    <custom-modal
      :visible="visible"
      :data="fileDetail"
      @close="handleClose"
      @save="handleSave"
      :Permission="Permission"
    ></custom-modal>
  </div>
</template>
  <script>
import {
  uploadFile,
  getSuccessFiles,
  getUnauditedFiles,
  getFileDetail,
} from "api/file";
import CustomModal from "components/CustomModal.vue";
export default {
  name: "UploadFile",
  components: { CustomModal },
  data() {
    return {
      value: "",
      options: [
        {
          value: "literature",
          label: "literature",
        },
        {
          value: "biology",
          label: "biology",
        },
        {
          value: "medicine",
          label: "medicine",
        },
      ],
      tableDate: [],
      fileList: [],
      success_files: [],
      wait_examine_files: [],
      total1: 0,
      params1: {
        //设置初始值
        currentpage: 1,
        pageSize: 4,
      },
      total2: 0,
      params2: {
        //设置初始值
        currentpage: 1,
        pageSize: 4,
      },
      visible: false,
      title: "编辑文献",
      fileDetail: {},
      Permission: {
        Onlyread: true,
        examine: false,
      },
    };
  },
  computed: {
    getField() {
      return this.value;
    },
    isSelected() {
      return !this.value.length > 0;
    },
  },
  methods: {
    submit() {
      //逐个文件上传
      this.fileList.forEach((file) => {
        uploadFile({
          title: file.title,
          content: file.content,
          field: file.field,
        }).then((res) => {
          if (res.code == 200) {
            this.$message.success("上传成功");
            this.fileList = [];
          } else {
            this.$message.error(res.msg);
          }
        });
      });
      this.getSuccessFiles();
    },
    beforeUpload(file) {
        console.log(file.name.split(".")[1])
      //读取文件名和内容并且添加到fileList中
      if (file.name.split(".")[1] != "txt") {
        this.$message.error("文件类型错误，只能上传txt文件");
      } else {
        const reader = new FileReader();
        reader.readAsText(file);
        reader.onload = (e) => {
          this.fileList.push({
            title: file.name.split(".")[0],
            content: e.target.result,
            field: this.getField,
          });
        };
      }
    },
    uploadFile(file, fileList) {},
    handleChange(value) {},
    handleSizeChange1(v) {
      this.params1.pageSize = v;
      this.getSuccessFiles();
    },
    handleCurrentChange1(v) {
      this.params1.currentpage = v;
      this.getSuccessFiles();
    },
    handleSizeChange2(v) {
      this.params2.pageSize = v;
      this.getUnauditedFiles();
    },
    handleCurrentChange2(v) {
      this.params2.currentpage = v;
      this.getUnauditedFiles();
    },
    getSuccessFiles() {
      getSuccessFiles(this.params1).then((res) => {
        if (res.code == 200) {
          this.success_files = res.data.data;
          this.total1 = res.data.total;
          console.log(this.total);
        }
      });
    },
    getUnauditedFiles() {
      getUnauditedFiles(this.params2).then((res) => {
        if (res.code == 200) {
          this.wait_examine_files = res.data.data;
          this.total2 = res.data.total;
        }
      });
    },
    getFileDetail(document_id) {
      getFileDetail({ document_id: document_id }).then((res) => {
        if (res.code == 200) {
          this.fileDetail = res.data;
        }
      });
    },
    handdle1(row) {
      this.visible = true;
      this.getFileDetail(row.document_id);
      this.Permission.Onlyread = !this.$store.getters.getIdentity;
      this.Permission.examine = false;
    },
    handdle2(row) {
      this.visible = true;
      this.getFileDetail(row.document_id);
      this.Permission.Onlyread = false;
      this.Permission.examine = true;
    },
    handleClose() {
      this.visible = false;
    },
    handleSave(data) {
      this.visible = false;
    },
  },
  created() {
    //获取已经上传的文件
    this.getSuccessFiles();
    this.getUnauditedFiles();
  },
};
</script>
<style scoped>
.block :deep(.el-cascader) {
  width: 170px;
}
.block {
  margin-top: 20px;
}
h3 {
  float: left;
  width: 442px;
  padding: 0 10px;
}
.demo-form-inline li {
  display: table-cell;
  float: left;
  margin: 20px 10px;
  width: 240px;
  height: 148px;
  display: inline;
  list-style: none;
  padding: 0;
}
.demo-form-inline li .el-button {
  margin-top: 20px;
}
.demo-form-inline .tishi {
  margin-right: 50px;
  font-size: small;
}
.file_list {
  margin: 30px;
}
.pagination1 {
  position: absolute;
  bottom: 50px;
  left: 300px;
}
.pagination2 {
  position: absolute;
  bottom: 50px;
  right: 450px;
}
.el-table::before {
  z-index: inherit;
}
.shangchuan {
  border-radius: 20px;
  background-color: #5e85bf;
  color: #fff;
}
</style>
 