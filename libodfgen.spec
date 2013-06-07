#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	Library to generate ODF documents from libwpd and libwpg API calls
Summary(pl.UTF-8):	Biblioteka do generowania dokumentów ODF z wywołań API libwpd i libwpg
Name:		libodfgen
Version:	0.0.2
Release:	1
License:	MPL v2.0 or LGPL v2.1+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/libwpd/%{name}-%{version}.tar.xz
# Source0-md5:	b2fc76996a2a4e2aba32c9be18fb903c
URL:		http://libwpd.sourceforge.net/
BuildRequires:	autoconf >= 2.65
BuildRequires:	automake >= 1:1.11
BuildRequires:	boost-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:2
BuildRequires:	libwpd-devel >= 0.9
BuildRequires:	libwpg-devel >= 0.2
BuildRequires:	pkgconfig >= 1:0.20
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	libwpd >= 0.9
Requires:	libwpg >= 0.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library to generate ODF documents from libwpd and libwpg API calls.

%description -l pl.UTF-8
Biblioteka do generowania dokumentów ODF z wywołań API libwpd i
libwpg.

%package devel
Summary:	Header files for libodfgen library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libodfgen
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel
Requires:	libwpd-devel >= 0.9
Requires:	libwpg-devel >= 0.2

%description devel
Header files for libodfgen library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libodfgen.

%package static
Summary:	Static libodfgen library
Summary(pl.UTF-8):	Statyczna biblioteka libodfgen
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libodfgen library.

%description static -l pl.UTF-8
Statyczna biblioteka libodfgen.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{?with_static_libs:--enable-static} \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libodfgen-*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_libdir}/libodfgen-0.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libodfgen-0.0.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libodfgen-0.0.so
%{_includedir}/libodfgen-0.0
%{_pkgconfigdir}/libodfgen-0.0.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libodfgen-0.0.a
%endif
