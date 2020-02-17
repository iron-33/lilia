<template>
<div  class="Coments">
    <h1>Пример вывода комментариев</h1>
    <hr /><br><br><br><br>
    <p>Комментарии к статье</p>
    <form name="form">
        <p>Текст сообщения:<br><textarea name="message" rows="5" cols="50" id="message"></textarea></p>
        <input name="js" type="hidden" value="no" id="js">
        <p><input name="button" type="submit" value="Отправить" id="send"> <span id="resp"></span></p>
    </form>
</div>
</template>
<script>
export default {
  name: 'Coments',
data() {
    return {
      coments: [],
    }
  },
  methods:{
    comentShow(){
        return this.$emit('getComentsProducts')
    }
  }
  }
</script>