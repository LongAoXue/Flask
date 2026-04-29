// 给注册页面的“确认密码”加校验
window.onload = function() {
    const form = document.querySelector('form');
    if (form) {
        form.onsubmit = function(e) {
            const password = this.querySelector('input[name="password"]').value;
            const repassword = this.querySelector('input[name="repassword"]').value;
            
            if (password !== repassword) {
                alert("两次输入的密码不一致！");
                e.preventDefault(); // 阻止表单提交
            }
        }
    }
}