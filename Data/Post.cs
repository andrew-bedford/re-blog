using System.Dynamic;
using System.Text;
using System.Text.RegularExpressions;
using Markdig;
using Markdig.Extensions.Yaml;
using Markdig.Syntax;
using Microsoft.AspNetCore.Components;

namespace Re.Blog.Data
{
    class Post
    {
        public string Id { get; set; }
        public string Title { get; set; } = "";
        public string Path { get; set; }
        public string Abstract { get; set; } = "";
        public IEnumerable<string> Tags { get; set; } = new List<string>();
        public DateTime? Created { get; set; }
        public DateTime? Modified { get; set; }

        public string Markdown { get; set; }
        public string Html { get; set; }
        public string TableOfContents { get; set; } = "";

        public Post(string path, string markdown)
        {
            this.Path = path;
            this.Markdown = markdown;
            var pipeline = new MarkdownPipelineBuilder()
                                .UsePragmaLines()
                                .UseAdvancedExtensions()
                                .UseYamlFrontMatter()
                                .Build();
            this.Html = Markdig.Markdown.ToHtml(markdown, pipeline);

            // Parse document to extract tags
            var document = Markdig.Markdown.Parse(this.Markdown, pipeline);
            var yaml = document.Descendants<YamlFrontMatterBlock>().FirstOrDefault();
            if (yaml != null)
            {
                string[] yamlLines = this.Markdown.Substring(yaml.Span.Start, yaml.Span.Length).Split('\n');
                foreach (var line in yamlLines)
                {
                    if (line.StartsWith("id:"))
                    {
                        this.Id = line.Split("id:")[1].Trim().ToLower();
                    }
                    if (line.StartsWith("title:"))
                    {
                        this.Title = line.Split("title:")[1].Trim();
                    }
                    else if (line.StartsWith("abstract:"))
                    {
                        this.Abstract = line.Split("abstract:")[1].Trim();
                    }
                    else if (line.StartsWith("created:"))
                    {
                        System.Globalization.CultureInfo provider = System.Globalization.CultureInfo.InvariantCulture;
                        var date = line.Split("created:")[1].Trim();
                        this.Created = DateTime.ParseExact(date, "yyyy-MM-dd", provider);
                    }
                    else if (line.StartsWith("tags:"))
                    {
                        this.Tags = line.Split("tags:")[1].Split(",").Select(t => t.Trim());
                    }
                }
            }

            if (this.Id == null)
            {
                // FIXME: This assumes that the posts are not in subfolders and have a file extension, which is not necessarily true.
                this.Id = this.Path.Split(".")[0];
            }

            BuildTableOfContents();
        }

        public void BuildTableOfContents()
        {
            if (this.Markdown == null) { return; }

            StringBuilder builder = new();
            builder.AppendLine("[toc]");

            foreach (string line in this.Markdown.Split("\n").Select(line => line.TrimStart()))
            {
                if (Regex.IsMatch(line, "^#"))
                {
                    Console.WriteLine(line);
                    builder.AppendLine(line);
                }
            }

            var pipeline = new MarkdownPipelineBuilder()
                                .UseTableOfContent()
                                .Build();
            this.TableOfContents = Markdig.Markdown.ToHtml(builder.ToString(), pipeline).Split("\n").First();
            this.TableOfContents = this.TableOfContents.Replace("<a href='#", "<a href='javascript:scrollTo(\"");
            this.TableOfContents = this.TableOfContents.Replace("'>", "\")'>");
        }
    }
}