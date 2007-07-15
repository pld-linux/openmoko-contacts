Summary:	OpenMoko contacts applet
Summary(pl.UTF-8):	Aplet kontaktów dla OpenMoko
Name:		openmoko-contacts
Version:	0.0.0.2360
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	ef9ab9b63ef199e0dfda46166e77ae7e
URL:		http://openmoko.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 2:2.10.7
BuildRequires:	intltool
BuildRequires:	libmatchbox-devel >= 1.8
BuildRequires:	openmoko-libs-devel
Requires(post,preun):	GConf2
Requires:	openmoko-icons
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenMoko contacts applet.

%description -l pl.UTF-8
Aplet kontaktów dla OpenMoko.

%prep
%setup -q

%build
cp /usr/share/automake/mkinstalldirs .
%{__libtoolize}
%{__intltoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install contacts.schemas

%preun
%gconf_schema_uninstall contacts.schemas

%files
%defattr(644,root,root,755)
%{_sysconfdir}/gconf/schemas/contacts.schemas
%attr(755,root,root) %{_bindir}/contacts
%{_desktopdir}/contacts.desktop
%{_pixmapsdir}/openmoko-contacts.png
