import facebook
import json

ACCESS_TOKEN="EAAFb2YmyZAZCMBAHVelhmy7ULFJN94CeXpEsHcOtgqGkftBnpQfuSxxJBWWabHKv9mZA1baqIlABgqgDYm5fpZBc2iKvRQgFQOaQZCtxb4fFwIUPx3iOSLPm3gk2zGgm5aeMG1ziA38Im7AWqWAwydthbIkszBXLbnwk7TjNsjDNXkNrYbSP83PIhB2q7MWXhaY47gPLwfZCtCNEVDzHoTtT0nNKpxtzJHD3KkLw6yeAZDZD"

graph = facebook.GraphAPI(ACCESS_TOKEN)
profile = graph.get_object('me',fields='id,last_name,name,name_format,about')
print("Printing profile")
print(type(profile))
print(json.dumps(profile,indent=4))
print(type(json.dumps(profile,indent=4)))
