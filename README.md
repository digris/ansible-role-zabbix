Ansible Role for Zabbix
========================


Requirements
------------

 - Debian 8.x
   + Debian < 8.x: We don't have any reasons to support older versions.
   + ubuntu: Should/could work as well, but has never been tested.

Role Variables
--------------

- `abcd`: abcd, defasults to `no`



Example Playbook
----------------

Minimal usage example:

    - hosts: zabbix
      roles:
        - {
            role: digris.zabbix,
          }




Post Install Steps
------------------


License
-------

BSD
