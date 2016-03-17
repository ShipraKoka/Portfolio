using Microsoft.Owin;
using Owin;

[assembly: OwinStartupAttribute(typeof(AskaPortfolio.Startup))]
namespace AskaPortfolio
{
    public partial class Startup
    {
        public void Configuration(IAppBuilder app)
        {
            ConfigureAuth(app);
        }
    }
}
