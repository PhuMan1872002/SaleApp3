from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin,BaseView,expose
from app import app,db
from app.models import Category, Product
class MyProductView(ModelView):
    column_list = ['id','name','price','category_id']
    column_searchable_list = ['name']
    column_filters = ['price','name']
    can_export = True
    can_view_details = True
    column_editable_list = ['name']
class MycategoryView(ModelView):
    column_list = ['name','product']
class MyStatsView(BaseView):
    @expose("/")
    def __index__(self):
        return self.render('admin/stats.html')

admin=Admin(app=app,name='Quản Trị Bán hàng',template_mode='bootstrap3')
admin.add_view(MyProductView(Product,db.session))
admin.add_view(MycategoryView(Category, db.session))
admin.add_view(MyStatsView(name='Thống kê báo cáo'))