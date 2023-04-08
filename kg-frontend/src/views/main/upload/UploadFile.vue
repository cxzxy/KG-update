<template>
  <div>
    <el-upload
      class="upload-demo"
      :before-upload="beforeUpload"
      action=""
      :http-request="uploadFile"
      multiple
      :limit="10"
      :file-list="fileList"
      accept=".txt"
      :disabled="isSelected"
    >
      <el-button size="small" type="primary">选择文件</el-button>
      <div slot="tip" class="el-upload__tip">只能上传txt文件,且不超过4GB</div>
    </el-upload>
    <el-button type="primary" @click="submit">上传</el-button>
    <div class="block">
      <el-cascader
        v-model="value"
        class="el-cascader"
        placeholder="请选择文献领域"
        :options="options"
        @change="handleChange"
      ></el-cascader>
    </div>
    已审核通过文献
    <el-table
      :data="success_files"
      style="width: 100%">
      <el-table-column
        prop="title"
        label="文献名"
        width="180">
      </el-table-column>
      <el-table-column
        prop="field"
        label="文献领域"
        width="180">
      </el-table-column>
      <el-table-column
        prop="create_time"
        label="上传时间">
      </el-table-column>
    </el-table>
  </div>
</template>
<script>
import { uploadFile ,getSuccessFiles} from "api/file";
export default {
  name: "UploadFile",
  components: {},
  data() {
    return {
      value: "",
      options: [
        {
          value: "literature",
          label: "文学",
        },
        {
          value: "biology",
          label: "生物学",
        },
        {
          value: "medicine",
          label: "医学",
        },
      ],
      fileList: [],
      success_files: [],
    };
  },
  computed: {
    getField() {
      return this.value[0];
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
    },
    beforeUpload(file) {
      //读取文件名和内容并且添加到fileList中
      console.log(this.value.length);
      const reader = new FileReader();
      reader.readAsText(file);
      reader.onload = (e) => {
        this.fileList.push({
          title: file.name.split(".")[0],
          content: e.target.result,
          field: this.getField,
        });
      };
      return false;
    },
    uploadFile(file, fileList) {},
    handleChange(value) {
    },
  },
  async created() {
    //获取已经上传的文件
    const res = await getSuccessFiles();
    if (res.code == 200) {
      this.success_files = res.data;
      console.log(this.success_files)
    }
  },
};
</script>
<style scoped>
.block >>> .el-cascader {
  width: 170px;
}
.block {
  margin-top: 20px;
}
</style>
