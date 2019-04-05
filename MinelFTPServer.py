#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer


yonetici = DummyAuthorizer()
yonetici.add_anonymous("C:/sunucu", perm="elradfmw")
yonetici.add_user("minnela", "italy", "C:/sunucu", perm="elradfmw")
yonetici.add_user("sixfinger", "Angela Fortunata", "C:/sunucu", perm="elradfmw")

print("bitti")


# In[ ]:


handler = FTPHandler
handler.authorizer = yonetici
server = FTPServer(("127.0.0.1", 1200), handler)
server.serve_forever()

print("bitti")


# In[ ]:




