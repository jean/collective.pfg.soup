
History
=======

1.7.dev0
-----
- fixed autoinclude, Plone 5 compatibility
  [agitator]


1.6
-----

- prevent re-edit javscript from fetching cached requests. fixes #7
  [jensens, 2014-03-07]

- allow shared soup storage based on soup_name
  [agitator, 2014-12-16]

- added json response headers
  [agitator, 2014-12-16]

1.5
---

- deal with Rating Scale Field. fixes #6.
  [jensens, 2013-12-19]

1.4
---

- workaround in order to fix #5 On copy soup is not copied.
  [jensens, 2013-12-19]

1.3
---

- fixes #4 Export with non-ascii in labels fails.
  [jensens, 2013-12-16]

1.2
---

- fixes some problems in form re-edit mechanism. Before this change a form
  lost its data if a user clicked on view tab with edit cookie set already.
  Also re-edit resulted in double entries in some cases. With this change also
  issue #1 was fixed, which was in fact a side effect of the above.
  [jensens, 2013-09-16]

1.1.1
-----

- fixes broken release because of some git confusion
  [jensens, 2013-09-11]

1.1
---

- broken release, tries to: fix a bug while showing history.
  [jensens, 2013-08-26]

1.0
---

- added feature: delete rows
  [jensens, 2013-03-07]

1.0-beta3
---------

1.7 (unreleased)


- Nothing changed yet.


1.6 (2014-12-16)
  [jensens, 2013-02-24]

1.0-beta2
---------

- bugfix: subscriber raised AttributeError: get_soup [jensens, 2012-09-07]

1.0-beta
--------

- make it work [jensens, 2012-07-03]
