using Microsoft.AspNetCore.Components;
using MudBlazor;

namespace Re.Blog.Data
{
    static class Application
    {
        public static List<Post> Posts = new();
        public static MudTheme DefaultTheme = new()
        {
            Typography = new Typography()
            {
                Default = new Default()
                {
                    FontFamily = new[] { "Inter", "Ubuntu", "Helvetica", "Arial", "sans-serif" }
                }
            },

            Palette = new PaletteLight()
            {
                Background = "#FFFFFF",
                DrawerBackground = "#FFFFFF",
                AppbarBackground = "#FFFFFF",
                AppbarText = "#3B454E",
                TextPrimary = "#3B454E",
                Primary = "#2D3F55"
            }
        };

        public static bool IsRightDrawerOpen = false;
    }
}